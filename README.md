# RAG with pgvectorscale and PostgreSQL
This is a RAG project that was made from the tutorial at [this](https://www.youtube.com/watch?v=hAdEuDBN57g) link, with logs written to a folder. The original GitHub repo can be found [here](https://github.com/daveebbelaar/pgvectorscale-rag-solution/tree/setup).

## Steps to run
1. Clone the repository.
2. Create a file named `.env` in the `app/` folder and insert the following content:
```
OPENAI_API_KEY=<your OpenAI API key>
TIMESCALE_SERVICE_URL=postgres://postgres:password@localhost:5432/postgres
```
3. Create a folder named `logs` in the root folder.
4. Create a Python virtual environment named `venv`, activate it and use `pip install -r requirements.txt` to install the dependencies.
5. Navigate to the `docker/` folder and run the following command to start the Docker container:
```
docker compose up -d
```
6. Using a PostgreSQL client (for example, the VS Code extension), make a connection with the following details:
    * Host: localhost
    * Port: 5432
    * User: postgres
    * Password: password
    * Database: postgres
7. Run the demo code in `app/demo.ipynb` to test the RAG functionality.
