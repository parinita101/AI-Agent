class RecursiveCharacterTextSplitter:
    def __init__(self, chunk_size=500, chunk_overlap=50):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def split_text(self, text):
        """Split text into chunks with overlap."""
        chunks = []
        start = 0
        text_length = len(text)

        while start < text_length:
            end = min(start + self.chunk_size, text_length)
            chunk = text[start:end]
            chunks.append(chunk)
            start += self.chunk_size - self.chunk_overlap

        return chunks

    def split_documents(self, documents):
        """Assuming documents is a list of objects with a 'page_content' attribute."""
        all_chunks = []
        for doc in documents:
            text = getattr(doc, 'page_content', str(doc))
            chunks = self.split_text(text)
            # Optionally convert each chunk into a document-like dict/object
            for chunk in chunks:
                all_chunks.append({"page_content": chunk})
        return all_chunks
