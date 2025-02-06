import requests

def fetch(query):

    base_url = "https://rest.uniprot.org/uniprotkb/search"
    params = {"query": query,"format": "json","size": 100}
    
    response = requests.get(base_url, params=params)

    if response.status_code == 200:

        data = response.json()
        results = data.get("results", [])
        
        if not results: return {"error": "No protein data found for the given query."}

        highest_annotation_result = None
        highest_annotation_score = -1
        
        for result in results:

            annotation_score = result.get("annotationScore", 0)

            if annotation_score > highest_annotation_score:
                highest_annotation_score = annotation_score
                highest_annotation_result = result
        
        result = highest_annotation_result
        result = {
            "UniProt ID": result.get("primaryAccession", "N/A"),
            "Protein Name": result.get("proteinDescription", {}).get("recommendedName", {}).get("fullName", {}).get("value", "N/A"),
            "Gene Name": result.get("genes", [{}])[0].get("geneName", {}).get("value", "N/A"),
            "Protein Length": result.get("sequence", {}).get("length", "N/A"),
            "Annotation Score": result.get("annotationScore", "N/A"),
            "Protein Sequence": result.get("sequence", {}).get("value", "N/A")
        }
        return result
    
    else:
        return {
            "error": f"Failed to fetch data. HTTP Status Code: {response.status_code}",
            "response_text": response.text
        }

if __name__ == "__main__":
    query = "AT4G40030.2"
    query = "AT5G59870.1"
    result = fetch(query)

    # Print all results
    if "error" in result:
        print(result["error"])
        if "response_text" in result:
            print(f"API Response: {result['response_text']}")
    else:
        print("Results:")
        for key, value in result.items():
            print(f"  {key}: {value}")
        print()
    