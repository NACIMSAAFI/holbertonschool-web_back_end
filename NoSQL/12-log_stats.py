#!/usr/bin/env python3
"""Provides statistics about Nginx logs stored in MongoDB"""

import pymongo


def log_stats():
    """Function to provide stats about Nginx logs stored in MongoDB"""
    # Connect to MongoDB server
    client = pymongo.MongoClient("mongodb://127.0.0.1:27017")

    # Access the logs database and the nginx collection
    db = client.logs
    nginx_collection = db.nginx

    # Get the total number of documents
    total_logs = nginx_collection.count_documents({})

    # Count the number of documents for each HTTP method
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {
        method: nginx_collection.count_documents({"method": method})
        for method in methods
    }

    # Count the number of documents with method=GET and path=/status
    status_check_count = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )

    # Print the results
    print(f"{total_logs} logs")
    print("Methods:")
    for method, count in method_counts.items():
        print(f"    method {method}: {count}")
    print(f"{status_check_count} status check")


if __name__ == "__main__":
    log_stats()
