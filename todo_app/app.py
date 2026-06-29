from flask import Flask, request, render_template, redirect
from todo import TodoApp

app = Flask(__name__)

todo = TodoApp([])
todo.load_tasks()

@app.route("/", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        task = request.form["task"]
        todo.add_task(task)
        todo.save_task()
        return redirect("/")
    return render_template("index.html", tasks=todo.tasks)

if __name__ == "__main__":
    app.run(debug=True)