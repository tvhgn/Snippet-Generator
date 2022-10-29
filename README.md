# Snippet-Generator
Generates snippets in vscode format
Uses content on clipboard to generate a snippet.

How-to:
1. Copy code that you want to turn into a snippet on your clipboard.
2. Run python script. Snippet will be automatically copied to user clipboard.
3. Paste code in your python.json snippets file in vscode.

--- Example: ---
1. Code copied on clipboard:
while True:
    try:
      print(x)
      break
    except:
      print('An exception occurred')

2. Running of python script.

3. Output, available on clipboard.
"while_try_block": {
		"prefix": "while_try_block",
		"body":
		[
			"while True:",
			"    try:",
			"      print(x)",
			"      break",
			"    except:",
			"      print('An exception occurred')",
		],
		"description": "Try-except block within a while loop. Can be used for catching errors without leaving a certain part of code."
    
Note: standard text for "description" is "No description yet"
