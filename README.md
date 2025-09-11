graph TD
    subgraph "Phase 1: Ingestion Pipeline (One-Time Setup)"
        direction TB
        style Ingestion fill:#f0f8ff,stroke:#b0c4de

        CSV[("fa:fa-file-csv 188,539-Word Dictionary.csv")] -->|1. Read Data| Ingest_Script(ingest.py)
        Ingest_Script -->|2. Process in Chunks| Pandas(Pandas DataFrame)
        Pandas -->|3. Create Text Docs| TextChunks["'Word: Aard-vark. Type: n...'"]
        TextChunks -->|4. Convert to Vectors| ST_Model_Ingest(Sentence Transformer Model)
        ST_Model_Ingest -->|5. Store Vectors & Text| ChromaDB[fa:fa-database ChromaDB Vector Database]
    end

    subgraph "Phase 2: Live Query Application (Real-Time Chat)"
        direction TB
        style Query fill:#f0fff0,stroke:#98fb98
        
        User(fa:fa-user User) -->|Asks a question: "mammal that eats ants?"| App(app.py / ask.py)
        App -->|A. Vectorize Query| ST_Model_Query(Sentence Transformer Model)
        ST_Model_Query -->|B. Find Similar Vectors| ChromaDB
        ChromaDB -->|C. Return Matching Document(s)| App
        App -->|D. Assemble Answer| Response["The most relevant entry is for 'Aard-vark'..."]
        Response -->|E. Display to User| User
    end

    style User fill:#d3d3d3,stroke:#000
    style Response fill:#e6e6fa,stroke:#9370db
