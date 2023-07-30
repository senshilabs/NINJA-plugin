# NINJA-plugin
![image](https://github.com/senshilabs/NINJA-plugin/assets/10369528/3172eef7-f346-401a-aaf0-9931d6b56daa)

NINJA, an acronym for "Ninja is an Interface for NFTs and a Junction of AI", is a project designed to seamlessly blend the worlds of blockchain technology and artificial intelligence, providing a powerful, no-code tool that caters to both industries.

![image](https://github.com/senshilabs/NINJA-plugin/assets/10369528/2b821923-a497-40dd-ad31-03fc9001da40)

## Overview

Welcome to the NINJA-plugin repository! The NINJA-plugin is a custom node developed for [ComfyUI](https://github.com/comfyanonymous/ComfyUI). 

## Structure
![image](https://github.com/senshilabs/NINJA-plugin/assets/10369528/05bf139f-e6a7-4faf-ba74-5b04d6470059)


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

NINJA-plugin is designed for expandability, and we have an exciting roadmap ahead. Our future plan includes:

 - **Support for Additional Blockchains**: We are working to extend our blockchain node to accommodate more chains, including but not limited to Sui, Near Protocol, etc.

 - **Support for More Transaction Types**: Currently, our nodes directly support read operations. We aim to include support for more transaction types, such as writing to contracts and triggering smart contract functions, etc.

 - **Enhancing Usability**: Our focus on user experience will drive us to make continuous improvements in the plugin's usability. We recognize that an intuitive and user-friendly interface is essential for widespread adoption, and we are committed to refining the existing features to make them more accessible to users of all levels.

 - **Full UX Integration**: Building on our efforts to enhance usability, we are planning a full integration of user experience design within the plugin. This means a concerted effort to align all aspects of the user's interaction with the plugin, ensuring that it not only meets functional needs but also provides an engaging and satisfying experience.


## Project Structure

The project adopts a clear and intuitive structure, segregating different functionalities into separate directories:

- `.init.py`: This file is crucial for defining the Python package. Here, we register the mappings for the node display name (NODE_DISPLAY_NAME_MAPPINGS) and node class (NODE_CLASS_MAPPINGS).

- `./service/`: This directory contains the core logic of the project, housing the actual implementations of the functionalities. It is further divided into subdirectories for specific tasks and features.

## Nodes
- `S3 Image Upload`: Used to upload images to S3
- `S3 Metadata Upload`: Used to upload OpenSea standard metadata to S3.
- `S3 File Upload`: Used to upload a file to S3.
- `Load AWS Config`: Used to load AWS-specific settings on the path if you do not want to expose security information such as AWS secret keys, etc.
- `Load Image HTTP or IPFS`: Used to load an image from HTTP or IPFS, it automatically determines the HTTP/IPFS path and loads the image.
- `Load Image From Metadata HTTP or IPFS`: Used to load an image from metadata on HTTP or IPFS. When you enter the URL of the metadata, it extracts the URL of the image contained in the metadata and returns the image.
- `Ether Read Image Path ERC721`: Returns the image path of an ERC721 token on the Ethereum network.
- `Astar Read Image Path ERC721`: Returns the image path of an ERC721 token on the Astar network.
- `Astar Read Image Path Payable Mint`: Returns the image path through the `PayableMint::token_uri` interface of a WASM-based contract on the Astar network.
- `Astar Read Attribute PSP43`: Returns an attribute via the `PSP43::get_attribute` interface of a WASM-based contract on the Astar network.
- `HttpCall`: Sends a request to a URL by entering the HTTP request method (GET, POST, etc.), URL, headers, body, etc.


## Workflow Example
- [Video](https://www.youtube.com/watch?v=hODK3rptbdk)

