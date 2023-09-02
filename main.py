from flask import Flask, jsonify
import json

app = Flask(__name__)

# Define your quiz data here
quiz_json = '''
{
  "A1": {
    "questions": {
      "1": {
        "statement": "How do you say 'The dog' in German?",
        "options": ["Der Hund", "Die Katze", "Den Hund", "Die Hund"],
        "right_answer": "Der Hund"
      },
      "2": {
        "statement": "What is 'hello' in German?",
        "options": ["Auf Wiedersehen", "Guten Tag", "Danke", "Bitte"],
        "right_answer": "Guten Tag"
      },
      "3": {
        "statement": "How do you say 'I am hungry' in German?",
        "options": [
          "Ich bin müde",
          "Ich habe Durst",
          "Ich habe Angst",
          "Ich habe Hunger"
        ],
        "right_answer": "Ich habe Hunger"
      },
      "4": {
        "statement": "What does 'Schule' mean in English?",
        "options": ["School", "House", "Car", "Tree"],
        "right_answer": "School"
      }
    }
  },
  "A2": {
    "questions": {
      "1": {
        "statement": "Translate 'The cat' to German.",
        "options": ["Der Hund", "Die Katze", "Die Maus", "Der Vogel"],
        "right_answer": "Die Katze"
      },
      "2": {
        "statement": "What does 'Apfel' mean in English?",
        "options": ["Banana", "Apple", "Orange", "Pear"],
        "right_answer": "Apple"
      },
      "3": {
        "statement": "Formal way to say 'you' in German?",
        "options": ["Du", "Er", "Sie", "Es"],
        "right_answer": "Sie"
      },
      "4": {
        "statement": "Translate 'Goodbye' to German.",
        "options": ["Guten Tag", "Auf Wiedersehen", "Danke", "Bitte"],
        "right_answer": "Auf Wiedersehen"
      }
    }
  },
  "B1": {
    "questions": {
      "1": {
        "statement": "Translate 'environment' to German.",
        "options": ["Umwelt", "Wetter", "Landschaft", "Natur"],
        "right_answer": "Umwelt"
      },
      "2": {
        "statement": "What is the past tense of 'essen'?",
        "options": ["Isst", "Esst", "Aß", "Essen"],
        "right_answer": "Aß"
      },
      "3": {
        "statement": "What is 'computer' in German?",
        "options": ["Rechner", "Fernseher", "Telefon", "Tisch"],
        "right_answer": "Rechner"
      },
      "4": {
        "statement": "Which German city is known for its carnival?",
        "options": ["Berlin", "Munich", "Cologne", "Hamburg"],
        "right_answer": "Cologne"
      }
    }
  },
  "B2": {
    "questions": {
      "1": {
        "statement": "What does 'Gesundheit' mean when someone sneezes?",
        "options": ["Good luck", "Bless you", "Health", "Excuse me"],
        "right_answer": "Health"
      },
      "2": {
        "statement": "What is the subjunctive II form of 'gehen'?",
        "options": ["Ich gehe", "Ich ginge", "Ich ging", "Ich werde gehen"],
        "right_answer": "Ich ginge"
      },
      "3": {
        "statement": "What is the German word for 'ambitious'?",
        "options": ["Ehrgeizig", "Abenteuerlich", "Vorsichtig", "Entspannt"],
        "right_answer": "Ehrgeizig"
      },
      "4": {
        "statement": "Who wrote 'Faust'?",
        "options": [
          "Johann Wolfgang von Goethe",
          "Friedrich Schiller",
          "Heinrich Heine",
          "Thomas Mann"
        ],
        "right_answer": "Johann Wolfgang von Goethe"
      }
    }
  }
}
'''

quiz = json.loads(quiz_json)
# print(quiz)

@app.route('/quiz/<level>/<int:question_number>', methods=['GET'])
def get_question(level, question_number):
    if level in quiz and str(question_number) in quiz[level]['questions']:
        return jsonify(quiz[level]['questions'][str(question_number)])
    else:
        return jsonify({"error": "Question not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
