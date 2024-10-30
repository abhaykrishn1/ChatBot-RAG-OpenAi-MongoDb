from embeddings.vector_embedding import generate_embeddings
from embeddings.vector_search import search, print_results
from embeddings.summarize_results import process_and_summarize
from utils.logger import main_logger
from database.mongodb_connection import MongoDBConnection

def main():
    main_logger.info("Starting the application")

    # Generate embeddings for all documents
    # Uncomment to generate embeddings
    # main_logger.info("Generating embeddings for all documents")
    # generate_embeddings()

    # Perform a test search
    # user_query = "what car models are available in white?"
    user_query = input("please ask a question ...  ")
    main_logger.info(f"Performing test search with query: {user_query}")
    results = search(user_query)

    if results:
        main_logger.info(f"Found {len(results)} results for test query")
        print_results(results)              # print the results to the console

        # Summarize the results
        main_logger.info("Summarizing search results")
        summary = process_and_summarize(user_query, results)
        print(f"Query: {user_query}")
        print("\nSummary:")
        print(summary)

        # Log the summary
        main_logger.info(f"Summary: {summary}")
    else:
        main_logger.warning("No results found for test query")
        print("No results found.")

    

    # Close MongoDB connection
    MongoDBConnection.get_instance().close_connection()
    main_logger.info("Application finished")

if __name__ == "__main__":
    main()