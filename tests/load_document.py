    # Load multiple text files from a directory successfully
    def test_load_multiple_text_files(self):
        # Arrange
        test_dir = "test_docs"
        os.makedirs(test_dir, exist_ok=True)
        with open(f"{test_dir}/file1.txt", "w") as f1, open(f"{test_dir}/file2.txt", "w") as f2:
            f1.write("Content 1")
            f2.write("Content 2")
    
        # Act
        docs = load_documents(test_dir)
    
        # Assert
        assert len(docs) == 2
        assert any("Content 1" in doc.page_content for doc in docs)
        assert any("Content 2" in doc.page_content for doc in docs)
    
        # Cleanup
        shutil.rmtree(test_dir)