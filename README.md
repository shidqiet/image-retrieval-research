# Image Retrieval Research

### Research Question:
What is the cheapest and fastest method for image retrieval, given the constraints of limited computation (serverless containers) and a need for fast responses (i.e., the calculation of image hashes/descriptors/embeddings should not be repeated on each user request)?

### Additional Questions:
- How about video retrieval?

### Initial Answer:
- To check for exact matches, we can use checksums (MD5, SHA-256).
- However, if the image has been slightly modified, it's better to use perceptual hash-based methods.
- Content-based approaches, such as those using embeddings, are resource-intensive.
- Additionally, methods like SIFT generate high-dimensional descriptors, which also require substantial computational resources to compute similarities.
