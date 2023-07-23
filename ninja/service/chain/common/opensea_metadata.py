def make_metadata(image_path, description=None, external_url=None, name=None):
    metadata = {
        "description": description,
        "external_url": external_url,
        "image": image_path,
        "name": name,
        "attributes": []
    }

    return {k: v for k, v in metadata.items() if v is not None}
