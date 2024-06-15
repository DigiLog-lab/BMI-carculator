from flask import Flask, request, render_template

app = Flask(__name__)

#入力する画面を表示
@app.route('/')
def home():
    return render_template('home.html')

#入力された値を受け取り、BMIを計算して結果を表示
@app.route('/carculate', methods=['POST'])
def carculate():
    #身長
    height = request.form['height'] 
    #体重
    weight = request.form['weight']
    #BMIを計算
    result = float(weight) / (float(height) ** 2)
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)

    