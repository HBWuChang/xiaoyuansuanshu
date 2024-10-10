from flask import Flask, request
import json
import time
import keyboard
import threading

app = Flask(__name__)


@app.route("/", methods=["POST"])
def 服务器():
    # print(request.data)
    jsons = json.loads(request.data.decode())
    print(jsons)
    '''{
        "pkIdStr": "608977381113270368",
        "otherUser": {
            "userId": 1053342400,
            "userName": "大学也得学",
            "avatarUrl": "https://leo-online.fbcontent.cn/leo-gallery/16a9fd213b2ce7f.png",
            "userPendantUrl": None,
        },
        "otherWinCount": 0,
        "selfWinCount": 8,
        "targetCostTime": 10000,
        "examVO": {
            "pkIdStr": "608977381113270368",
            "pointId": 2,
            "pointName": "20以内数的比大小",
            "ruleType": 0,
            "questionCnt": 10,
            "correctCnt": 0,
            "costTime": 0,
            "questions": [
                {
                    "id": 0,
                    "examId": 608977381113270368,
                    "content": "12\\circle3",
                    "answer": ">",
                    "userAnswer": None,
                    "answers": [">"],
                    "status": 0,
                    "script": None,
                    "wrongScript": None,
                    "ruleType": "COMPARE",
                },
                {
                    "id": 1,
                    "examId": 608977381113270368,
                    "content": "16\\circle7",
                    "answer": ">",
                    "userAnswer": None,
                    "answers": [">"],
                    "status": 0,
                    "script": None,
                    "wrongScript": None,
                    "ruleType": "COMPARE",
                },
                {
                    "id": 2,
                    "examId": 608977381113270368,
                    "content": "14\\circle8",
                    "answer": ">",
                    "userAnswer": None,
                    "answers": [">"],
                    "status": 0,
                    "script": None,
                    "wrongScript": None,
                    "ruleType": "COMPARE",
                },
                {
                    "id": 3,
                    "examId": 608977381113270368,
                    "content": "9\\circle11",
                    "answer": "<",
                    "userAnswer": None,
                    "answers": ["<"],
                    "status": 0,
                    "script": None,
                    "wrongScript": None,
                    "ruleType": "COMPARE",
                },
                {
                    "id": 4,
                    "examId": 608977381113270368,
                    "content": "15\\circle11",
                    "answer": ">",
                    "userAnswer": None,
                    "answers": [">"],
                    "status": 0,
                    "script": None,
                    "wrongScript": None,
                    "ruleType": "COMPARE",
                },
                {
                    "id": 5,
                    "examId": 608977381113270368,
                    "content": "4\\circle8",
                    "answer": "<",
                    "userAnswer": None,
                    "answers": ["<"],
                    "status": 0,
                    "script": None,
                    "wrongScript": None,
                    "ruleType": "COMPARE",
                },
                {
                    "id": 6,
                    "examId": 608977381113270368,
                    "content": "20\\circle12",
                    "answer": ">",
                    "userAnswer": None,
                    "answers": [">"],
                    "status": 0,
                    "script": None,
                    "wrongScript": None,
                    "ruleType": "COMPARE",
                },
                {
                    "id": 7,
                    "examId": 608977381113270368,
                    "content": "13\\circle8",
                    "answer": ">",
                    "userAnswer": None,
                    "answers": [">"],
                    "status": 0,
                    "script": None,
                    "wrongScript": None,
                    "ruleType": "COMPARE",
                },
                {
                    "id": 8,
                    "examId": 608977381113270368,
                    "content": "11\\circle3",
                    "answer": ">",
                    "userAnswer": None,
                    "answers": [">"],
                    "status": 0,
                    "script": None,
                    "wrongScript": None,
                    "ruleType": "COMPARE",
                },
                {
                    "id": 9,
                    "examId": 608977381113270368,
                    "content": "3\\circle14",
                    "answer": "<",
                    "userAnswer": None,
                    "answers": ["<"],
                    "status": 0,
                    "script": None,
                    "wrongScript": None,
                    "ruleType": "COMPARE",
                },
            ],
            "updatedTime": 0,
        },
    }'''
    tasks = jsons["examVO"]["questions"]
    threading.Thread(target=进程, args=(tasks,)).start()
    return json.dumps({"status": "done"})


def 进程(tasks):
    time.sleep(12.3)
    for task in tasks:
        match task["answer"]:
            case ">":
                keyboard.press("1")
                time.sleep(0.13)
                keyboard.release("1")
            case "<":
                keyboard.press("2")
                time.sleep(0.25)
                keyboard.release("2")
            case _:
                pass
        time.sleep(0.25)
    time.sleep(5)
    keyboard.press_and_release("3")
    time.sleep(0.6)
    keyboard.press_and_release("4")
    time.sleep(0.6)
    keyboard.press_and_release("5")


app.run("0.0.0.0", 24101, debug=True)