from flask import Flask, render_template # type: ignore
import sync_tool

app = Flask(__name__)

@app.route('/')
def index():
    # Call the sync_tool to get the latest status
    sync_tool.main()  #Basically for running the synchronization process
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
