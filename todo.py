#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
from datetime import datetime, timezone

def help() :
    return "Usage :-\n$ ./todo add \"todo item\"  # Add a new todo\n$ ./todo ls               # Show remaining todos\n$ ./todo del NUMBER       # Delete a todo\n$ ./todo done NUMBER      # Complete a todo\n$ ./todo help             # Show usage\n$ ./todo report           # Statistics"

def addTask(task) :
    prev = ""
    with open('todo.txt', 'r+') as todo :
        prev = todo.read()
        print(prev)
    if len(prev) :
        prev = "\n"+prev
    with open('todo.txt', 'w') as todo :
        todo.write(task+prev)
    return 'Added todo: "' + task + '"'

def ls():
    todos = []
    with open('todo.txt', 'r') as todo :
        todos = todo.readlines()
    if not len(todos) :
        print("There are no pending todos!",end='')
    for i in range(len(todos)) :
        print( "[%i] %s" %(len(todos)-i, todos[i]), end='' )
    print()
    
def delete(taskNo) :
    try:
        todos = []
        with open('todo.txt', 'r') as todo :
            todos = todo.readlines()
        if not 0<taskNo<=len(todos) :
            raise ValueError
        del todos[-taskNo]
        with open('todo.txt', 'w') as todo :
            todo.writelines(todos)
    except:
        return "Error: todo #"+str(taskNo)+" does not exist. Nothing deleted."
    else :
        return "Deleted todo #"+str(taskNo)
    
def markDone(taskNo) :
    todos = []
    task = ""
    with open('todo.txt', 'r') as todo :
        todos = todo.readlines()
    try:
        if not 0<taskNo<=len(todos) :
            raise ValueError
        task = todos[-taskNo]
        del todos[-taskNo]
        with open('todo.txt', 'w') as todo :
            todo.writelines(todos)
    except:
        return "Error: todo #"+str(taskNo)+" does not exist. Nothing deleted."
    else :
        did = ''
        with open('done.txt', 'r') as done :
            did = done.read()
        if len(did) :
            did = "\n"+did
        with open('done.txt', 'w') as done :
            done.write("x %s %s%s" %(datetime.now(timezone.utc).strftime("%Y-%m-%d"),task,did) )
        return "Marked todo #" + str(taskNo) + " as done."

def report() :
    pending,completed = 0,0
    with open('todo.txt', 'r') as todo :
        pending = len(todo.readlines())
    with open('done.txt', 'r') as done :
        completed = len(done.readlines())-1
    return datetime.now(timezone.utc).strftime("%Y-%m-%d") + " Pending : " + str(pending) + " Completed : " +str(completed)

def main() :
    args = sys.argv

    if len(args) == 1:
        print(help())

    elif args[1] == 'help':
        if len(args) == 2:
            print(help())
        else:
            print('Too Many Arguments for help! Please use "./todo help" for Usage Information')
    elif args[1] == 'ls':
        if len(args) == 2:
            ls()
        else:
            print('Too Many Arguments for ls! Please use "./todo help" for Usage Information')

    elif args[1] == 'add':
        if len(args) == 3:
            print(addTask(args[2]))
        else:
            print('Error: Missing todo string. Nothing added!')

    elif args[1] == 'del':
        if len(args) == 3:
            print(delete(int(args[2])))
        else:
            print('Error: Missing NUMBER for deleting todo.')
    elif args[1] == 'done':
        if len(args) == 3:
            print(markDone(int(args[2])))
        else:
            print('Error: Missing NUMBER for marking todo as done.')

    elif args[1] == 'report':
        if len(args) == 2:
            print(report(),end='')
        else:
            print('Too Many Arguments for report! Please use "./todo help" for Usage Information')
    else:
        print('Option Not Available. Please use "./todo help" for Usage Information')

if not os.path.isfile('todo.txt'):
    with open("todo.txt","w") as f:
        pass
if not os.path.isfile('done.txt'):
    with open("done.txt","w") as f:
        pass
main()