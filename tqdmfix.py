import json

notebook_path = "MCH_chatbot.ipynb"  # change this to your file

with open(notebook_path, "r", encoding="utf-8") as f:
    notebook = json.load(f)

# Remove widgets metadata if it exists
if "widgets" in notebook.get("metadata", {}):
    del notebook["metadata"]["widgets"]

# Save the cleaned notebook
with open(notebook_path, "w", encoding="utf-8") as f:
    json.dump(notebook, f, indent=1)

print("✅ Removed 'metadata.widgets' from notebook.")
