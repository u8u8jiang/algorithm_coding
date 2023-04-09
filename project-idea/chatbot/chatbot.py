from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer     
import spacy

# 1、创建一个聊天机器人：将bot作为输入参数, 並返回一个对象, Jill。        

def create_bot(name):
    Bot = ChatBot(name=name, read_only = False, 
                  logic_adapters = ["chatterbot.logic.BestMatch"],
                  storage_adapter = "chatterbot.storage.SQLStorageAdapter")
    return Bot

# 2、训练聊天机器人：输入参数bot, 正在训练聊天机器人的数据显示在这里.
def train_all_data(Bot):
    corpus_trainer = ChatterBotCorpusTrainer(Bot)
    corpus_trainer.train("chatterbot.corpus.english")

# 3、使用自定义数据训练：输入参数為bot本身, 和要训练的自定义数据list輸入。
# 列表的第一个元素是问题，第二个元素是答案, 可以使用盡可能多的特定自定义数据来训练聊天机器人。
def custom_train(Bot, conversation):
    trainer = ListTrainer(Bot)
    trainer.train(conversation)

# 4、启动聊天机器人：输入参数bot, 是我们要启动的
def start_chatbot(Bot):
    print('\033c')
    print("Hello, I am Jill. How can I help you")
    bye_list = ["bye Jill","bye","good bye"]
    
    while(True):
        user_input = input("me:")
        if user_input.lower()in bye_list:
            print("Jill: Good bye and have a blessed day!")
        break

    response=Bot.get_response(user_input)
    print(":",response)
    print("Jill:",response)

def main():
    spacy.load("en_core_web_sm")
    bot = create_bot("Jill")
    train_all_data(bot)
    start_chatbot(bot)


if __name__ == "__main__":
    main()

