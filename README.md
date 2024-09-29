# **Blog: Integrating Blockchain for Authentic Post Ownership in Django Based Blog Application**

A modern blog application built using Django, which integrates blockchain technology to verify post ownership. This innovative approach ensures the authenticity and integrity of blog posts, making it a unique platform for writers and readers alike.

## **Technologies Used**

- **Django**: Web framework for building the backend.
- **Python**: Programming language for application development.
- **Solidity**: Language for writing smart contracts on the Ethereum blockchain.
- **Ganache**: Personal blockchain for Ethereum development.
- **Remix IDE**: Integrated development environment for Solidity smart contracts.
- **Web3.py**: Python library for interacting with the Ethereum blockchain.
- **SQLite3**: Lightweight database for data storage.

## **Features**

- **Post Management**: Create, view, and manage blog posts with ease.
- **Ownership Tracking**: Each post includes **"OWNER"** and **"TRANSACTION HASH"** fields in the model, allowing for clear ownership identification.
- **Blockchain Integration**: The presence of a **"BLOCK NUMBER"** in the post model indicates the use of a blockchain system to verify and record ownership.
- **Functional Display**: The Django admin interface accurately displays ownership information, providing administrators with insights into post ownership.
- **Categorization**: Organize posts into categories for better navigation.
- **Search Functionality**: Quickly find posts using a search feature.

## **Blockchain Integration**

This project incorporates Solidity smart contracts to establish blog post ownership on the blockchain. The smart contract code is located in the `blogpostownership.sol` file.

### **Steps for Blockchain Interaction:**

1. **Local Blockchain**: Use Ganache to set up a local blockchain environment.
2. **Smart Contract Deployment**: Deploy the smart contract using Remix IDE.
3. **Application Interaction**: Utilize Web3.py to interact with the smart contract from the Django application, enabling ownership verification for each blog post.

## **Setup and Installation**

To set up and run the project locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/crashblog.git
   cd crashblog
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up the Database**:
   ```bash
   python manage.py migrate
   ```

5. **Create a Superuser** (optional):
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```

7. **Access the Application**: Open your web browser and navigate to `http://127.0.0.1:8000/`.

### **Blockchain Environment Setup**

1. **Install Ganache**: Download and install Ganache from the [official site](https://www.trufflesuite.com/ganache).
2. **Deploy Smart Contract**: Open Remix IDE and load the `blogpostownership.sol` file. Compile and deploy the contract to the Ganache blockchain.
3. **Connect Web3.py**: Ensure that Web3.py is configured to connect to your local Ganache instance.

## **Usage**

- **Creating Blog Posts**: Log in and navigate to the post creation page to start writing.
- **Verifying Ownership**: After creating a post, the ownership can be verified through the blockchain by interacting with the smart contract via the application interface.

## **Contributing**

Contributions are welcome! To contribute to the project:
1. **Fork the Repository**: Create your own copy of the repository.
2. **Create a New Branch**: Use a descriptive branch name.
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make Your Changes**: Implement your feature or fix.
4. **Submit a Pull Request**: Describe the changes you've made.

## **License**

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for more details.

---
