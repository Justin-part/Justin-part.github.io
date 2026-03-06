import urllib.request
import json
import os

req = urllib.request.Request("https://joftjvzbphcihndmrsvg.supabase.co/rest/v1/reviews?select=*", headers={"apikey": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImpvZnRqdnpicGhjaWhuZG1yc3ZnIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzEzOTM3MjYsImV4cCI6MjA4Njk2OTcyNn0.45_A2YcoA27svdZJ5HEDmUY-3HMTqFYts8ty-30k55U", "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImpvZnRqdnpicGhjaWhuZG1yc3ZnIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzEzOTM3MjYsImV4cCI6MjA4Njk2OTcyNn0.45_A2YcoA27svdZJ5HEDmUY-3HMTqFYts8ty-30k55U"})
res = urllib.request.urlopen(req)
data = json.loads(res.read())
print(f"Total reviews: {len(data)}")
if len(data) > 0:
  print(f"Sample review: {data[0]}")
