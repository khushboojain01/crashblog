from django.db.models import Q
from django.shortcuts import get_object_or_404, render, redirect
from .models import Post, Category
from .forms import CommentForm, BlogPostForm
from web3 import Web3
from web3.exceptions import Web3Exception

# Connect to Ganache
ganache_url = "http://127.0.0.1:7545"  # Replace with your local Ganache instance URL
web3 = Web3(Web3.HTTPProvider(ganache_url))


# Check if connection to Ganache is successful
try:
    # Use block_number instead of blockNumber
    latest_block = web3.eth.get_block('latest')
    print(f"Connected to Ganache. Latest block number: {latest_block['number']}")
    GANACHE_CONNECTED = True
except Web3Exception as e:
    print(f"Connection to Ganache failed: {str(e)}")
    GANACHE_CONNECTED = False
except Exception as e:
    print(f"An unexpected error occurred: {str(e)}")
    GANACHE_CONNECTED = False

# Only set up the contract if Ganache is connected
if GANACHE_CONNECTED:
    contract_address = '0x9A1cE018bB8DFE79f1CFF7a249E0092CE7A842ab'  # Replace with your deployed contract address
    abi = [
    {
        "anonymous": False,  # Change false to False
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "owner",
                "type": "address"
            },
            {
                "indexed": True,
                "internalType": "uint256",
                "name": "postId",
                "type": "uint256"
            },
            {
                "indexed": False,
                "internalType": "bytes32",
                "name": "postHash",
                "type": "bytes32"
            }
        ],
        "name": "BlogPostStored",
        "type": "event"
    },
    {
        "inputs": [
            {
                "internalType": "bytes32",
                "name": "postHash",
                "type": "bytes32"
            }
        ],
        "name": "storeHash",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "blogCount",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "name": "blogPosts",
        "outputs": [
            {
                "internalType": "address",
                "name": "owner",
                "type": "address"
            },
            {
                "internalType": "bytes32",
                "name": "postHash",
                "type": "bytes32"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "postId",
                "type": "uint256"
            }
        ],
        "name": "getBlogPostHash",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            },
            {
                "internalType": "bytes32",
                "name": "",
                "type": "bytes32"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    }
]
    contract = web3.eth.contract(address=contract_address, abi=abi)
else:
    contract = None

# Blog post detail view
def detail(request, category_slug, slug):
    post = get_object_or_404(Post, slug=slug, status=Post.ACTIVE)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('post_detail', category_slug=category_slug, slug=slug)
    else:
        form = CommentForm()

    return render(request, 'blog/detail.html', {'post': post, 'form': form})

# Category view
def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = category.posts.filter(status=Post.ACTIVE)
    return render(request, 'blog/category.html', {'category': category, 'posts': posts})

# Search view
def search(request):
    searchquery = request.GET.get('query', '')
    posts = Post.objects.filter(status=Post.ACTIVE).filter(
        Q(title__icontains=searchquery) |
        Q(intro__icontains=searchquery) |
        Q(body__icontains=searchquery)
    )
    return render(request, 'blog/search.html', {'posts': posts, 'query': searchquery})

def frontpage(request):
    posts = Post.objects.filter(status=Post.ACTIVE)
    return render(request, 'core/frontpage.html', {'posts': posts})

# Create blog post with blockchain interaction
def create_blog_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            blog_post = form.save(commit=False)
            
            if GANACHE_CONNECTED:
                try:
                    # Hash the post content
                    post_hash = web3.keccak(text=blog_post.body)
                    
                    # HexBytes object is already in the correct format for bytes32
                    # No need for conversion
                    
                    # Simulating an account (from Ganache)
                    account = web3.eth.accounts[0]  # Replace with MetaMask account for real use

                    # Store the hash on the blockchain
                    transaction = contract.functions.storeHash(post_hash).transact({
                        'from': account,
                        'gas': 2000000
                    })

                    # Wait for transaction receipt
                    receipt = web3.eth.wait_for_transaction_receipt(transaction)

                    # Store blockchain details in Django
                    blog_post.owner = account
                    blog_post.transaction_hash = receipt['transactionHash'].hex()
                    blog_post.block_number = receipt['blockNumber']
                    blog_post.save()

                    return redirect('frontpage')
                except Exception as e:
                    print(f"Blockchain interaction failed: {str(e)}")
                    return render(request, 'blog/create_blog_post.html', {
                        'form': form,
                        'message': f'Blog post saved, but blockchain verification failed: {str(e)}'
                    })
            else:
                blog_post.save()
                return render(request, 'blog/create_blog_post.html', {
                    'form': form, 
                    'message': 'Blog post saved, but blockchain verification is currently unavailable.'
                })
    else:
        form = BlogPostForm()

    return render(request, 'blog/create_blog_post.html', {'form': form})

# Verify ownership of the blog post on blockchain
def verify_ownership(request, post_id):
    blog_post = get_object_or_404(Post, id=post_id)

    if GANACHE_CONNECTED:
        try:
            # Hash the post content
            post_hash = web3.toHex(web3.keccak(text=blog_post.body))

            # Retrieve the stored hash from the blockchain
            owner, stored_hash = contract.functions.getBlogPostHash(post_id).call()

            if post_hash == stored_hash:
                status = "Ownership verified!"
            else:
                status = "Ownership could not be verified."
        except Exception as e:
            status = f"Verification failed due to an error: {str(e)}"
    else:
        status = "Blockchain verification is currently unavailable."

    return render(request, 'verify_ownership.html', {'status': status, 'blog_post': blog_post})