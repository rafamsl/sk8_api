<!-- GETTING STARTED -->
## Getting Started

This is my second commited project. It is a basic API to track your progress while skating

You will be able to:

1. Create a new skate trick in your collection
2. Get your performance stats for a trick
3. Edit your performance stats for a trick
4. Delete a trick from your collection

### Installation


1. Clone the repo

2. Install fastapi and uvicorn packages
   ```
   pip3 install fastapi
   pip3 install uvicorn
   ```


<!-- USAGE EXAMPLES -->
## Usage

1. Starting the app

After installing, you should start the app in your project with the command:

```uvicorn main:app --reload```   ({app} is the name of your ap)


2. Reading the docs

You can read the API docs in http://127.0.0.1:8000/docs

3. API calls

** They are all GET commands for now, because chrome throws 405 with other methods. **

3.1 Get Tricks

```http://127.0.0.1:8000/trick/Ollie```

Returns:
- {trick_name}  {correct_attempts}/{total_attemps}

3.2 Add Trick

```http://127.0.0.1:8000/new_trick/Kickflip```

if it does not exist, {trick_name} will be saved in your collection with 0/0 stats

3.3 Edit Trick

```http://127.0.0.1:8000/add_session/Ollie?corrects=1&total=1```

if the trick exists, it will add {corrects} and {total} to the current stats and return the final stats for that trick

if the trick doesn exist, it will be created with the added stats

3.4 Clean trick

```http://127.0.0.1:8000/clean_trick/Ollie```

if the trick exists, its stats are reseted to 0/0



