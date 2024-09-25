// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract BlogOwnership {
    struct BlogPost {
        address owner;
        bytes32 postHash;
    }

    mapping(uint => BlogPost) public blogPosts;
    uint public blogCount = 0;

    event BlogPostStored(address indexed owner, uint indexed postId, bytes32 postHash);

    // Store the hash of the blog post
    function storeHash(bytes32 postHash) public {
        blogPosts[blogCount] = BlogPost(msg.sender, postHash);
        emit BlogPostStored(msg.sender, blogCount, postHash);
        blogCount++;
    }

    // Retrieve the hash by ID
    function getBlogPostHash(uint postId) public view returns (address, bytes32) {
        BlogPost memory post = blogPosts[postId];
        return (post.owner, post.postHash);
    }
}
