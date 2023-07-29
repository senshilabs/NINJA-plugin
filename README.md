# NINJA-plugin

NINJA, an acronym for "Ninja is an Interface for NFTs and a Junction of AI", is a project designed to seamlessly blend the worlds of blockchain technology and artificial intelligence, providing a powerful, no-code tool that caters to both industries.

## Overview

Welcome to the NINJA-plugin repository! The NINJA-plugin is a custom node developed for [ComfyUI](https://github.com/comfyanonymous/ComfyUI). 

## How to Use

1. Start by cloning this repository or downloading the code.
2. Proceed to copy the custom node Python files into your ComfyUI project (located in ComfyUI\custom_nodes).
3. Install the necessary dependencies via pip in ComfyUI's environment.
4. Run ComfyUI.

## Current Capabilities and Future Developments

The NINJA-plugin presently supports:

1. **AWS Node**: Facilitates seamless interaction with AWS services, primarily supporting file and image uploads to AWS S3.

2. **HTTP Node**: Enables communication with web servers and APIs via HTTP requests.

3. **Blockchain Node**: Capable of interacting with specific blockchain contracts. It currently supports Ethereum and Astar.
   - **Ethereum Node**: Can fetch image paths(`http` / `ipfs`) from Ethereum ERC721 contracts.
   - **Astar Node**: Capable of extracting image paths(`http` / `ipfs`) from Astar PSP34 contracts.

## Upcoming Extensions

NINJA-plugin is designed for expandability. Our future plan includes:

- **Support for additional blockchains**: We are working to extend our blockchain node to accommodate more chains, including but not limited to Sui, Near Protocol, etc.

- **Support for more transaction types**: Currently, our nodes directly support read operations. We aim to include support for more transaction types, such as writing to contracts and triggering smart contract functions, etc.

## Project Structure

The project adopts a clear and intuitive structure, segregating different functionalities into separate directories:

- `.init.py`: This file is crucial for defining the Python package. Here, we register the mappings for the node display name (NODE_DISPLAY_NAME_MAPPINGS) and node class (NODE_CLASS_MAPPINGS).

- `./service/`: This directory contains the core logic of the project, housing the actual implementations of the functionalities. It is further divided into subdirectories for specific tasks and features.

## Workflow Example
- TBD
