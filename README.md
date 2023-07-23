# NINJA-plugin

[Ninja is an Interface for NFTs and a Junction of AI] in comfyUI

## Description

Welcome to the NINJA-plugin repository! 

NINJA, short for "Ninja is an Interface for NFTs and a Junction of AI", is a project designed to seamlessly blend the worlds of blockchain technology and artificial intelligence, providing a powerful, no-code tool that caters to both industries.

The NINJA-plugin is a custom node designed for [ComfyUI](https://github.com/comfyanonymous/ComfyUI). ComfyUI users can leverage NINJA's functionalities right from their GUI, benefiting from NINJA's blockchain and AI capabilities without writing a single line of code.

## Usage
1. Clone this repository or download the code.
2. Copy the custom node Python files into your ComfyUI project (ComfyUI\custom_nodes).
3. Install dependency via pip in ComfyUI's evn
4. Run ComfyUI


# Current Features and Future Scope
## Node Categories
The NINJA-plugin currently supports the following features:

1. **AWS Node**: Allows for smooth interaction with AWS services. Specifically, it supports file and image uploads to AWS S3.

2. **HTTP Node**: Facilitates communication with web servers and APIs by sending HTTP requests.

3. **Blockchain Node**: This node is capable of interacting with specific blockchain contracts, currently supporting Ethereum and Astar.
   - **Ethereum Node**: The Ethereum node can read image paths from Ethereum ERC721 contracts.
   - **Astar Node**: The Astar node can extract image paths from Astar PSP34 contracts.

## Planned Extensions

The NINJA-plugin is designed to be extensible and we plan to support additional chains and transactions in the future. This includes but is not limited to:

- **Support for more blockchains**: We plan to extend our blockchain node to support more chains like Sui, Near Protocol, etc.

- **Support for more transactions**: Currently, our nodes only directly support read operations. We plan to extend this to directly support more types of transactions, such as writing to contracts and triggering smart contract functions, etc.


# Project Structure
The project is organized in a clear, intuitive structure that divides up the different functionalities into separate directories:

`.init.py`: This file plays a crucial role in the Python package definition. Here, we register the mappings for the node display name (NODE_DISPLAY_NAME_MAPPINGS) and node class (NODE_CLASS_MAPPINGS).

`./service/`: This directory is a package containing the actual implementations of the functionalities. Here is where the core logic of the project resides and is further divided into subdirectories for specific tasks and features.


# Workflow Example
- TBD
