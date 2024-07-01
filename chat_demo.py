from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="gemini-pro")


# チャットのデモ関数
def chat_demo():
    print("チャットデモを開始します。終了するには 'exit' と入力してください。\n")
    while True:
        user_input = input("あなた: ")
        if user_input.lower() == "exit":
            print("チャットを終了します。")
            break
        # Geminiモデルを使用して応答を生成（仮のメソッド名）
        response = llm.conversation(input=user_input)
        print(f"AI: {response}")


# デモの実行
if __name__ == "__main__":
    chat_demo()
