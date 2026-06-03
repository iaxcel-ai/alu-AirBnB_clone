# AirBnB Clone - The Console

## Project Overview

This is the first phase of building a full-stack AirBnB clone. The goal here is to build a command-line interpreter that manages the lifecycle of AirBnB objects (creating, reading, updating, and deleting them) while persisting data to a JSON file between sessions.

### Models

| Class         | Purpose                                                                |
| ------------- | ---------------------------------------------------------------------- |
| `BaseModel`   | Parent class that handles id generation, timestamps, and serialization |
| `User`        | Stores user credentials and profile info                               |
| `State`       | Represents a geographic state                                          |
| `City`        | A city linked to a state                                               |
| `Place`       | A rental listing                                                       |
| `Amenity`     | A feature or amenity for a place                                       |
| `Review`      | A user review for a place                                              |
| `FileStorage` | Serializes/deserializes all objects to `file.json`                     |

---

## The Console

The console is the entry point for interacting with the application. It runs in both interactive and non-interactive mode.

### Starting the Console

**Interactive:**

```bash
./console.py
```

**Non-interactive:**

```bash
echo "<command>" | ./console.py
```

### Supported Commands

| Command   | Usage                                | Description                                         |
| --------- | ------------------------------------ | --------------------------------------------------- |
| `create`  | `create <class>`                     | Creates a new instance, saves it, and prints the id |
| `show`    | `show <class> <id>`                  | Prints the string representation of an instance     |
| `destroy` | `destroy <class> <id>`               | Deletes an instance permanently                     |
| `all`     | `all [class]`                        | Lists all instances, or all of a specific class     |
| `update`  | `update <class> <id> <attr> <value>` | Updates an attribute on an instance                 |
| `quit`    | `quit`                               | Exits the console                                   |
| `EOF`     | `Ctrl+D`                             | Exits the console                                   |
| `help`    | `help [command]`                     | Shows available commands or details on one          |

---

## Usage Examples

**Interactive session:**

```
$ ./console.py
(hbnb) create User
b6a6e15c-c67d-4312-9a75-9d084935e579
(hbnb) show User b6a6e15c-c67d-4312-9a75-9d084935e579
[User] (b6a6e15c-c67d-4312-9a75-9d084935e579) {'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', ...}
(hbnb) update User b6a6e15c-c67d-4312-9a75-9d084935e579 first_name "Ishimwe"
(hbnb) all User
["[User] (b6a6e15c-c67d-4312-9a75-9d084935e579) {...}"]
(hbnb) destroy User b6a6e15c-c67d-4312-9a75-9d084935e579
(hbnb) quit
$
```

**Non-interactive:**

```
$ echo "create BaseModel" | ./console.py
(hbnb) 49faff9a-6318-451f-87b6-910505c55907
(hbnb)
$ echo "all" | ./console.py
(hbnb) []
(hbnb)
```

---

## Author

Ishimwe Axcel - [i.axcel@alustudent.com](mailto:i.axcel@alustudent.com)
