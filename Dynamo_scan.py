#This code will be used to scan a dynamodb table.
#Importing boto3 libraries for AWS use.
import boto3
#Attaching variables to Dynamodb and to my table.
dynamodb = boto3.resource('dynamodb')
table_name = dynamodb.Table('Favorite_Games')
response = table_name.scan()
#Printing the results from scanning the table.
print(response)
