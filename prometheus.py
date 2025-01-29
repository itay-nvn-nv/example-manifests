import requests
import json
from urllib.parse import quote

def run_prometheus_query(prometheus_url, query):
    """
    Runs a Prometheus query via the API.

    Args:
        prometheus_url (str): The URL of your Prometheus server (e.g., "http://localhost:9090").
        query (str): The Prometheus query string.

    Returns:
        dict or None: The JSON response from the API or None if there's an error.
    """
    url = f"{prometheus_url}/api/v1/query"
    params = {"query": query}
    try:
      response = requests.get(url, params=params)
      response.raise_for_status() # Raise HTTPError for bad responses (4xx or 5xx)
      data = response.json()
      return data
    except requests.exceptions.RequestException as e:
        print(f"Error during Prometheus API call: {e}")
        return None
    except json.JSONDecodeError as e:
         print(f"Error decoding JSON: {e}")
         return None

def main():
    # Define your Prometheus Server
    prometheus_server = "http://localhost:9090"  # Replace with your Prometheus server address
    # Define your Query
    prometheus_query = 'sum(rate(container_cpu_usage_seconds_total{container!=""}[2m])) by (pod, namespace)'

    # Run the query, and parse the output
    result = run_prometheus_query(prometheus_server, prometheus_query)

    if result:
        print("Prometheus Query Result:")
        print(json.dumps(result, indent=2))  # Pretty print the JSON output
        if result.get('data'): # if there is any data in the result
           for res in result['data'].get('result',[]):
              print(f"Pod: {res['metric'].get('pod','N/A')}, Namespace: {res['metric'].get('namespace','N/A')}, CPU Utilization (cores/sec): {res.get('value','N/A')}")
    else:
         print("Failed to fetch prometheus data")

if __name__ == "__main__":
    main()
