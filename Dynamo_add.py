#This code will add items to my DynamoDB Table.
#Importing boto3 libraries for AWS use.
import boto3
#Connecting a variable to our dynamodb client.
dynamodb = boto3.client("dynamodb")
#Using batch_write_item so we can add multiple items all at once. 
response = dynamodb.batch_write_item(
    RequestItems = {
#The syntax after RequestedItems is our table name then listing the items to add
        "Favorite_Games": [
            {
                "PutRequest": {
                    "Item": {
                        "Title": {
                            "S": "Far Cry 3",
                            },
                        },
                    },
                },
            {
                "PutRequest": {
                    "Item": {
                        "Title": {
                            "S": "Spider-Man(PS4)",
                            },
                        },
                    },
                },
            {
                "PutRequest": {
                    "Item": {
                        "Title": {
                            "S": "The Legend of Zelda: Breath of the Wild",
                            },
                        },
                    },
                },
            {
                "PutRequest": {
                    "Item": {
                        "Title": {
                            "S": "Mario Kart 8",
                            },
                        },
                    },
                },
            {
                "PutRequest": {
                    "Item": {
                        "Title": {
                            "S": "Super Mario Odyssey",
                            },
                        },
                    },
                },
            {
                "PutRequest": {
                    "Item": {
                        "Title": {
                            "S": "Doom(2016)",
                            },
                        },
                    },
                },
            {
                "PutRequest": {
                    "Item": {
                        "Title": {
                            "S": "Star Wars Jedi: Fallen Order",
                            },
                        },
                    },
                },
            {
                "PutRequest": {
                    "Item": {
                        "Title": {
                            "S": "Horizon Zero Dawn",
                            },
                        },
                    },
                },
            {
                "PutRequest": {
                    "Item": {
                        "Title": {
                            "S": "Minecraft",
                            },
                        },
                    },
                },
            {
                "PutRequest": {
                    "Item": {
                        "Title": {
                            "S": "Red Dead Redemption 2",
                            },
                        },
                    },
                },
            ]
        }
    )
    
    