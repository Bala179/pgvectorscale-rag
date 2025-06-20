from datetime import datetime
from database.vector_store import VectorStore
from services.synthesizer import Synthesizer
from timescale_vector import client

# Initialize VectorStore
vec = VectorStore()

# --------------------------------------------------------------
# Shipping question
# --------------------------------------------------------------

relevant_question = "What are your shipping options?"
results = vec.search(relevant_question, limit=3)

response = Synthesizer.generate_response(question=relevant_question, context=results)

print(f"\n{response.answer}")
print("\nThought process:")
for thought in response.thought_process:
    print(f"- {thought}")
print(f"\nContext: {response.enough_context}")

# --------------------------------------------------------------
# Irrelevant question
# --------------------------------------------------------------

irrelevant_question = "What is the weather in Tokyo?"

results = vec.search(irrelevant_question, limit=3)

response = Synthesizer.generate_response(question=irrelevant_question, context=results)

print(f"\n{response.answer}")
print("\nThought process:")
for thought in response.thought_process:
    print(f"- {thought}")
print(f"\nContext: {response.enough_context}")

# --------------------------------------------------------------
# Metadata filtering
# --------------------------------------------------------------

metadata_filter = {"category": "Shipping"}

results = vec.search(relevant_question, limit=3, metadata_filter=metadata_filter)

response = Synthesizer.generate_response(question=relevant_question, context=results)

print(f"\n{response.answer}")
print("\nThought process:")
for thought in response.thought_process:
    print(f"- {thought}")
print(f"\nContext: {response.enough_context}")

# --------------------------------------------------------------
# Advanced filtering using Predicates
# --------------------------------------------------------------

predicates = client.Predicates("category", "==", "Shipping")
results = vec.search(relevant_question, limit=3, predicates=predicates)


predicates = client.Predicates("category", "==", "Shipping") | client.Predicates(
    "category", "==", "Services"
)
results = vec.search(relevant_question, limit=3, predicates=predicates)


predicates = client.Predicates("category", "==", "Shipping") & client.Predicates(
    "created_at", ">", "2024-09-01"
)
results = vec.search(relevant_question, limit=3, predicates=predicates)

# --------------------------------------------------------------
# Time-based filtering
# --------------------------------------------------------------

# June — Returning results
time_range = (datetime(2025, 6, 1), datetime(2025, 6, 30))
results = vec.search(relevant_question, limit=3, time_range=time_range)

# May — Not returning any results
time_range = (datetime(2025, 5, 1), datetime(2025, 5, 31))
results = vec.search(relevant_question, limit=3, time_range=time_range)