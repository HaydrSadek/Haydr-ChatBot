#!/usr/bin/env python3
"""
HaydrBot Pro v2.0
Multilingual AI Chatbot with Smart Knowledge Base
Built by Haydr - Computer & Control Engineering Graduate
"""

import random
import re
import sys

# ========================================================================
# KNOWLEDGE BASE - Smart facts with examples and real-life applications
# ========================================================================

KNOWLEDGE_BASE = {
    "en": {
        "physics": [
            {
                "title": "Einstein's General Relativity",
                "fact": "Time is not constant! It moves slower when you travel at high speeds or near massive objects.",
                "example": "If you flew on a plane for one year, you would be 0.000053 seconds younger than someone on the ground!",
                "application": "GPS satellites must adjust their clocks every day because time moves faster for them in orbit. Without this correction, GPS would drift by 10 km per day!"
            },
            {
                "title": "Quantum Gravity",
                "fact": "Gravity isn't actually a 'force' - it's the curvature of space-time caused by mass and energy!",
                "example": "Imagine placing a bowling ball on a trampoline. The ball creates a dip, and marbles roll toward it. That's how planets orbit the sun!",
                "application": "Black holes are the ultimate proof: they curve space-time so much that nothing, not even light, can escape!"
            },
            {
                "title": "Quantum Computing",
                "fact": "Quantum computers use 'qubits' that can be 0 and 1 at the same time, thanks to superposition!",
                "example": "A classical computer testing a 4-digit password tries 0000, 0001, 0002... A quantum computer tries ALL combinations simultaneously!",
                "application": "In 2019, Google's quantum computer solved a problem in 200 seconds that would take the world's fastest supercomputer 10,000 years!"
            }
        ],
        "space": [
            {
                "title": "Black Holes",
                "fact": "At the center of every black hole is a singularity - a point where density becomes infinite and physics breaks down!",
                "example": "If the Earth were compressed to the size of a marble, it would become a black hole with the same gravity!",
                "application": "The Event Horizon Telescope captured the first image of a black hole in 2019 (M87*), proving Einstein right once again!"
            },
            {
                "title": "The Expanding Universe",
                "fact": "The universe is not just expanding - the expansion is ACCELERATING, pushed by mysterious 'dark energy'!",
                "example": "Imagine dots on a balloon. As you inflate it, all dots move apart. But in our universe, the balloon is inflating faster and faster!",
                "application": "In 5 billion years, the Milky Way and Andromeda galaxies will collide. But by then, most other galaxies will have disappeared beyond our cosmic horizon!"
            },
            {
                "title": "Neutron Stars",
                "fact": "Neutron stars are so dense that one teaspoon of their material weighs 6 billion tons - as much as Mount Everest!",
                "example": "A neutron star the size of a city (20km wide) contains more mass than our entire Sun!",
                "application": "Pulsars (spinning neutron stars) are used as cosmic lighthouses and help us test Einstein's theories with extreme precision!"
            }
        ],
        "history": [
            {
                "title": "The Library of Alexandria",
                "fact": "The ancient Library of Alexandria held up to 700,000 scrolls - the entire knowledge of the ancient world in one place!",
                "example": "Eratosthenes calculated Earth's circumference there in 240 BC using just a stick and its shadow - and was only 2% off!",
                "application": "Its destruction (partially by fire, partially by neglect) set back human progress by centuries. It reminds us why preserving knowledge matters!"
            },
            {
                "title": "The Sumerians",
                "fact": "The Sumerians invented writing (cuneiform) around 3400 BC - not for poetry, but for accounting!",
                "example": "The oldest known written document is a clay tablet recording beer rations for workers. Even 5,000 years ago, people needed their paychecks!",
                "application": "They also invented the 60-base number system - that's why we have 60 seconds in a minute and 360 degrees in a circle!"
            },
            {
                "title": "The Antikythera Mechanism",
                "fact": "A 2,000-year-old Greek device is considered the world's first analog computer - it predicted eclipses and planetary positions!",
                "example": "It had over 30 bronze gears, some as small as 1mm, working together like a mechanical smartphone for astronomy!",
                "application": "It proves ancient civilizations had technology we thought was impossible until the 14th century. We still don't fully understand how they made it!"
            }
        ],
        "technology": [
            {
                "title": "The Internet's Origin",
                "fact": "The internet started as ARPANET in 1969 - originally designed to keep US military communication working during a nuclear attack!",
                "example": "The first message sent was 'LO' - they tried to type 'LOGIN' but the system crashed after two letters!",
                "application": "Today, 5.3 billion people use the internet. The protocol (TCP/IP) designed for nuclear war survival now carries cat videos and global commerce!"
            },
            {
                "title": "Artificial Intelligence",
                "fact": "Modern AI uses 'neural networks' inspired by the human brain - but GPT-4 has 1.8 trillion parameters, while the human brain has 86 billion neurons!",
                "example": "AI can now generate images from text (DALL-E), write code (GitHub Copilot), and even pass the bar exam - but it still can't reliably tell you if a picture contains a bird!",
                "application": "AI is used in medical diagnosis (detecting cancer better than doctors), climate modeling, and drug discovery - potentially saving millions of lives!"
            },
            {
                "title": "Quantum Encryption",
                "fact": "Quantum cryptography uses the laws of physics to create unbreakable encryption - if someone tries to intercept the key, the message self-destructs!",
                "example": "China launched the world's first quantum satellite (Micius) in 2016, successfully sending quantum-encrypted messages over 1,200 km!",
                "application": "Banks and governments are already testing quantum networks. In the future, all sensitive data could be protected by the laws of physics themselves!"
            }
        ],
        "biology": [
            {
                "title": "DNA Data Storage",
                "fact": "All the data ever created by humanity (about 120 zettabytes) could fit in a DNA strand the size of a shoebox!",
                "example": "In 2012, scientists encoded an entire book (53,000 words) into DNA - and then read it back with 99.99% accuracy!",
                "application": "Microsoft and others are developing DNA storage systems that could preserve data for 500,000+ years, surviving nuclear war and solar flares!"
            },
            {
                "title": "The Human Microbiome",
                "fact": "Your body contains about 39 trillion bacterial cells - slightly MORE than your 30 trillion human cells!",
                "example": "The bacteria in your gut weigh about 2 kg (4.4 lbs) - as much as your brain! They help digest food, produce vitamins, and even influence your mood!",
                "application": "Fecal transplants (transferring healthy gut bacteria) have cured deadly infections and are being tested for depression, autism, and obesity!"
            },
            {
                "title": "CRISPR Gene Editing",
                "fact": "CRISPR allows scientists to edit DNA with precision - like a 'find and replace' tool for genes!",
                "example": "In 2020, CRISPR cured sickle cell disease in a patient for the first time by editing their own cells. The patient is now symptom-free!",
                "application": "Scientists are developing CRISPR treatments for cancer, blindness, and HIV. Some even propose using it to bring back extinct species like woolly mammoths!"
            }
        ]
    },
    "ar": {
        "physics": [
            {
                "title": "النسبية العامة",
                "fact": "الزمن مش ثابت! بيمشي أبطأ لما بتسافر بسرعات عالية أو قرب أجسام ضخمة.",
                "example": "إذا طرت بالطيارة سنة كاملة، رح تكون أصغر بـ 0.000053 ثانية من اللي عالأرض!",
                "application": "أقمار GPS لازم تعدّل ساعاتها كل يوم لأن الزمن بيمشي أسرع لأنها بالفضاء. بدون هالتعديل، GPS رح يضلّ 10 كم باليوم!"
            },
            {
                "title": "الجاذبية الكمية",
                "fact": "الجاذبية مش 'قوة' فعلاً - هي انحناء الزمكان-الزمن بسبب الكتلة والطاقة!",
                "example": "تخيل كرة بولينج عالبساط. الكرة بتعمل حفرة، والكرات الصغيرة بتنزلق لعندها. هيك الكواكب بتدور حول الشمس!",
                "application": "الثقوب السوداء هي البرهان الأقوى: بتنحني الزمكان-الزمن كتير لدرجة إنه ولا شي، حتى الضوء، ما بيقدر يهرب!"
            },
            {
                "title": "الحواسيب الكمية",
                "fact": "الحواسيب الكمية بتستخدم 'كيوبتات' ممكن تكون 0 و 1 بنفس الوقت، بفضل التراكب!",
                "example": "الحاسوب العادي بيجرب كلمة سر 4 أرقام: 0000، 0001، 0002... الحاسوب الكمي بيجرب كل التركيبات بنفس الوقت!",
                "application": "بـ 2019، حاسوب Google الكمي حل مسألة بـ 200 ثانية كانت رح تاخد من أسرع حاسوب بالعالم 10,000 سنة!"
            }
        ],
        "space": [
            {
                "title": "الثقوب السوداء",
                "fact": "بمركز كل ثقب أسود فيه نقطة تفرد - نقطة الكثافة بتصير لانهائية والفيزياء بتتوقف!",
                "example": "إذا ضغطنا الأرض لحجم كرة رخام، رح تصير ثقب أسود بنفس الجاذبية!",
                "application": "تلسكوب Event Horizon صور أول صورة لثقب أسود بـ 2019 (M87*)، وبرهن إن Einstein كان محق مرة تانية!"
            },
            {
                "title": "توسع الكون",
                "fact": "الكون مش بس عم يتوسع - التوسع عم يتسارع، مدفوع بـ 'طاقة مظلمة' غامضة!",
                "example": "تخيل نقاط عبالونة. لما بتنفخها، كل النقاط بتبتعد. بس بكوننا، البالونة عم تنفخ أسرع وأسرع!",
                "application": "بـ 5 مليار سنة، مجرة درب التبانة وأندروميدا رح تصطدموا. بس وقتها، معظم المجرات التانية رح تختفي ورا الأفق الكوني!"
            },
            {
                "title": "النجوم النيوترونية",
                "fact": "النجوم النيوترونية كثيفة كتير إنه ملعقة صغيرة من مادتها بوزن 6 مليار طن - قد جبل إفرست!",
                "example": "نجم نيوتروني بحجم مدينة (20 كم) بيحتوي على كتلة أكبر من شمسنا كلها!",
                "application": "النجوم النابضة (اللي بتدور) مستخدمة كمنارات كونية وبساعدنا نختبر نظريات Einstein بدقة عالية!"
            }
        ],
        "history": [
            {
                "title": "مكتبة الإسكندرية",
                "fact": "مكتبة الإسكندرية القديمة كانت تحتوي على 700,000 لفافة - كل معرفة العالم القديم بمكان واحد!",
                "example": "Eratosthenes حسب محيط الأرض هنيك بـ 240 ق.م باستخدام عصا وظلها - وكان غلط بس 2%!",
                "application": "تدميرها (جزئياً بالنار، جزئياً بالإهمال) أخّر تقدم البشرية بقرون. بتذكرنا ليش حفظ المعرفة مهم!"
            },
            {
                "title": "السومريون",
                "fact": "السومريون اخترعوا الكتابة (المسمارية) حوالي 3400 ق.م - مش للشعر، للمحاسبة!",
                "example": "أقدم وثيقة مكتوبة معروفة هي لوح طين بيسجل حصص بيرة للعمال. حتى قبل 5,000 سنة، الناس كانوا بدّهم رواتبهم!",
                "application": "كمان اخترعوا نظام الأرقام بقاعدة 60 - لهيك عندنا 60 ثانية بالدقيقة و 360 درجة بالدائرة!"
            },
            {
                "title": "آلية أنتيكيثيرا",
                "fact": "جهاز يوناني عمره 2,000 سنة بيعتبر أول حاسوب تناظري بالعالم - كان بيتنبأ بالكسوفات ومواقع الكواكب!",
                "example": "كان فيه أكتر من 30 تروس برونزية، بعضهم بحجم 1 مم، عم يشتغلوا سوا متل سمارتفون ميكانيكي للفلك!",
                "application": "ببرهن إن الحضارات القديمة كان عندها تكنولوجيا فكرنا مستحيلة لـ القرن 14. لساتنا ما فهمنا كيف صنعوها!"
            }
        ],
        "technology": [
            {
                "title": "أصل الإنترنت",
                "fact": "الإنترنت بلش كـ ARPANET بـ 1969 - أصلاً مصمم ليحافظ على اتصالات الجيش الأمريكي وقت هجوم نووي!",
                "example": "أول رسالة مرسلة كانت 'LO' - حاولوا يكتبوا 'LOGIN' بس النظام وقع بعد حرفين!",
                "application": "اليوم، 5.3 مليار إنسان بيستخدموا الإنترنت. البروتوكول (TCP/IP) المصمم لحرب نووية هلأ بيحمل فيديوهات قطط وتجارة عالمية!"
            },
            {
                "title": "الذكاء الاصطناعي",
                "fact": "الذكاء الاصطناعي الحديث بيستخدم 'شبكات عصبية' مستوحاة من الدماغ البشري - بس GPT-4 عنده 1.8 تريليون معامل، بينما الدماغ البشري عنده 86 مليار خلية عصبية!",
                "example": "الذكاء الاصطناعي هلأ بيقدر يولد صور من نص (DALL-E)، يكتب كود (GitHub Copilot)، وحتى ينجح بامتحان المحاماة - بس لساته ما بيقدر يقلك بثقة إذا الصورة فيها طير!",
                "application": "بيستخدم بالتشخيص الطبي (اكتشاف السرطان أحسن من الأطباء)، نماذج المناخ، واكتشاف الأدوية - بيقدر ينقذ ملايين الأرواح!"
            },
            {
                "title": "التشفير الكمي",
                "fact": "التشفير الكمي بيستخدم قوانين الفيزياء لعمل تشفير غير قابل للكسر - إذا حدا حاول ياعترض المفتاح، الرسالة بتتدمّر ذاتياً!",
                "example": "الصين أطلقت أول قمر صناعي كمي (Micius) بـ 2016، ونجحت ترسل رسائل مشفرة كمياً لمسافة 1,200 كم!",
                "application": "البنوك والحكومات عم بتختبر شبكات كمية. بالمستقبل، كل البيانات الحساسة ممكن تكون محمية بقوانين الفيزياء نفسها!"
            }
        ],
        "biology": [
            {
                "title": "تخزين البيانات بالDNA",
                "fact": "كل البيانات يلي أنشأتها البشرية (حوالي 120 زيتابايت) ممكن تتساع بخيط DNA بحجم صندوق أحذية!",
                "example": "بـ 2012، العلماء شفروا كتاب كامل (53,000 كلمة) بـ DNA - وبعدين قرأوه بـ 99.99% دقة!",
                "application": "Microsoft وغيرهم عم يطوروا أنظمة تخزين DNA ممكن تحافظ على البيانات لـ 500,000+ سنة، وتنجو من حرب نووية وعواصف شمسية!"
            },
            {
                "title": "الميكروبيوم البشري",
                "fact": "جسمك بيحتوي على حوالي 39 تريليون خلية بكتيرية - أكتر شوي من 30 تريليون خلية بشرية!",
                "example": "البكتيريا بأمعائك بوزن حوالي 2 كغ - قد وزن دماغك! بيساعدوا بهضم الأكل، إنتاج الفيتامينات، وحتى التأثير على مزاجك!",
                "application": "زراعة البراز (نقل بكتيريا صحية) شافت إصابات مميتة وعم تُختبر للاكتئاب، التوحد، والسمنة!"
            },
            {
                "title": "تعديل الجينات بـ CRISPR",
                "fact": "CRISPR بيسمح للعلماء يعدلوا DNA بدقة - متل أداة 'بحث واستبدال' للجينات!",
                "example": "بـ 2020، CRISPR شافت مرض فقر الدم المنجلي لأول مرة بتعديل خلايا المريض نفسه. المريض هلأ بلا أعراض!",
                "application": "العلماء عم يطوروا علاجات CRISPR للسرطان، العمى، وHIV. بعضهم بيقترحوا استخدامها لإرجاع أنواع منقرضة متل الماموث الصوفي!"
            }
        ]
    }
}

# ========================================================================
# SPELL CORRECTION
# ========================================================================

SPELL_CORRECTIONS = {
    "en": {
        "physcs": "physics", "phisics": "physics", "fiziks": "physics",
        "fysics": "physics", "physis": "physics", "physic": "physics",
        "spase": "space", "spac": "space", "spece": "space",
        "spcae": "space", "sace": "space",
        "histoy": "history", "histry": "history", "histery": "history",
        "histroy": "history", "hisotry": "history",
        "tech": "technology", "teknology": "technology", "tecnology": "technology",
        "technolgy": "technology", "techology": "technology",
        "biolgy": "biology", "bioligy": "biology", "biologi": "biology",
        "bio": "biology", "byology": "biology",
        "helo": "hello", "hell": "hello", "helo": "hello",
        "thnks": "thanks", "thnx": "thanks", "thanx": "thanks",
        "thak": "thanks", "tanks": "thanks",
        "bye": "bye", "by": "bye", "bi": "bye",
        "exit": "exit", "quit": "exit", "close": "exit"
    },
    "ar": {
        "فزيا": "physics", "فيزي": "physics", "فيزك": "physics",
        "فضا": "space", "فض": "space",
        "تاري": "history", "تارخ": "history", "تريخ": "history",
        "تكنولوج": "technology", "تكنلوج": "technology", "تقنية": "technology",
        "احي": "biology", "احيا": "biology", "بيولوج": "biology",
        "مرحب": "hello", "هلا": "hello", "اهلا": "hello",
        "شكر": "thanks", "يسلمو": "thanks", "تسلم": "thanks",
        "مع السلامة": "bye", "باي": "bye", "سلام": "bye",
        "خروج": "exit", "سكر": "exit", "اطلع": "exit"
    }
}

# ========================================================================
# RESPONSES
# ========================================================================

RESPONSES = {
    "en": {
        "greetings": ["Hello!", "Hi there!", "Hey!", "Greetings!", "Welcome!"],
        "how_are_you": ["I'm doing great, thanks for asking!", "I'm excellent! Ready to share some knowledge.", "All systems go! What would you like to learn about?"],
        "thanks": ["You're very welcome!", "Anytime!", "My pleasure!", "Glad I could help!", "No problem at all!"],
        "goodbye": ["Goodbye! It was a great conversation.", "See you later! Keep curious!", "Take care! The universe is full of wonders waiting for you!", "Farewell! Remember: every question leads to a new discovery!"],
        "unknown": ["I'm not sure I understood that. Could you rephrase?", "Hmm, that's interesting! Could you tell me more?", "I didn't catch that. Try asking about Physics, Space, History, Technology, or Biology!"],
        "name_prompt": "What is your name? ",
        "name_response": "Nice to meet you, {name}! How can I help you today?",
        "topic_prompt": "\nI can tell you interesting facts about:\n  1. Physics\n  2. Space\n  3. History\n  4. Technology\n  5. Biology\n\nEnter a number (1-5) or type a topic name: ",
        "topic_error": "Please enter a number between 1 and 5, or type a topic name (physics, space, history, technology, biology).",
        "no_more_facts": "That's all I have about {topic} for now! Try another topic?",
        "facts_remaining": "({remaining} more fact(s) available about {topic})",
        "spell_corrected": "Did you mean '{corrected}'? Here's what I found:",
        "ask_more": "\nDid you like this fact? Want another example or a different topic?",
        "invalid_input": "I didn't understand that. Please try again."
    },
    "ar": {
        "greetings": ["أهلاً وسهلاً!", "مرحباً!", "هلا والله!", "أهلاً فيك!"],
        "how_are_you": ["منيح الحمدلله! شكراً على سؤالك.", "ممتاز! جاهز أشاركك معلومات شيقة.", "كلشي تمام! شو بدك تتعلم اليوم؟"],
        "thanks": ["العفو!", "أي وقت!", "تشرفت بمساعدتك!", "على الرحب والسعة!", "لا شكر على واجب!"],
        "goodbye": ["مع السلامة! كانت محادثة حلوة.", "بشوفك لاحقاً! خلي فضولك حي!", "الله معاك! الكون مليان عجائب عم تستنك!", "وداعاً! تذكر: كل سؤال بيوصلك لاكتشاف جديد!"],
        "unknown": ["مو متأكد فهمت عليك. ممكن توضح أكتر؟", "مثير للاهتمام! ممكن تحكيلي أكتر؟", "ما فهمت. جرب تسأل عن الفيزياء، الفضاء، التاريخ، التكنولوجيا، أو الأحياء!"],
        "name_prompt": "شو اسمك؟ ",
        "name_response": "منيح تعرفت عليك يا {name}! شو بدك نحكي فيه اليوم؟",
        "topic_prompt": "\nبقدر أحكيلك معلومات شيقة عن:\n  ١. الفيزياء\n  ٢. الفضاء\n  ٣. التاريخ\n  ٤. التكنولوجيا\n  ٥. الأحياء\n\nاكتب رقم (١-٥) أو اسم الموضوع: ",
        "topic_error": "رجاءً اكتب رقم بين ١ و ٥، أو اسم الموضوع (فيزياء، فضاء، تاريخ، تكنولوجيا، أحياء).",
        "no_more_facts": "خلصت معلوماتي عن {topic} للآن! بدك موضوع تاني؟",
        "facts_remaining": "(باقي {remaining} معلومة/معلومات عن {topic})",
        "spell_corrected": "قصدك '{corrected}'؟ هاي اللي لقيته:",
        "ask_more": "\nعجبتك المعلومة؟ بدك مثال تاني أو موضوع جديد؟",
        "invalid_input": "ما فهمت عليك. رجاءً جرب مرة تانية."
    }
}

TOPIC_MAP = {
    "en": {"1": "physics", "2": "space", "3": "history", "4": "technology", "5": "biology",
           "physics": "physics", "space": "space", "history": "history", "technology": "technology", "biology": "biology"},
    "ar": {"1": "physics", "2": "space", "3": "history", "4": "technology", "5": "biology",
           "١": "physics", "٢": "space", "٣": "history", "٤": "technology", "٥": "biology",
           "فيزياء": "physics", "الفيزياء": "physics", "فضاء": "space", "الفضاء": "space",
           "تاريخ": "history", "التاريخ": "history", "تكنولوجيا": "technology", "التكنولوجيا": "technology",
           "تقنية": "technology", "التقنية": "technology", "أحياء": "biology", "الأحياء": "biology",
           "بيولوجيا": "biology", "البيولوجيا": "biology"}
}

class HaydrBot:
    def __init__(self):
        self.lang = "en"
        self.user_name = ""
        self.shown_facts = {}  # Track shown facts per topic per session
        self.responses = RESPONSES
        self.knowledge = KNOWLEDGE_BASE
        self.spell = SPELL_CORRECTIONS
        self.topic_map = TOPIC_MAP

    def set_language(self, choice):
        if choice in ["1", "1.", "english", "en"]:
            self.lang = "en"
            print("\n✅ English selected!")
        elif choice in ["2", "2.", "arabic", "ar", "العربية", "عربي"]:
            self.lang = "ar"
            print("\n✅ تم اختيار العربية!")
        else:
            return False
        return True

    def get_response(self, key, **kwargs):
        resp = self.responses[self.lang].get(key, "")
        if isinstance(resp, list):
            resp = random.choice(resp)
        return resp.format(**kwargs) if kwargs else resp

    def correct_spelling(self, text):
        text_lower = text.lower().strip()
        corrections = self.spell.get(self.lang, {})

        # Direct match
        if text_lower in corrections:
            return corrections[text_lower], True

        # Fuzzy match - check if input is close to any correction key
        for wrong, correct in corrections.items():
            if wrong in text_lower or text_lower in wrong:
                if len(text_lower) >= 3:  # Only correct if input is at least 3 chars
                    return correct, True

        return text, False

    def detect_topic(self, text):
        text_lower = text.lower().strip()

        # Try spell correction first
        corrected, was_corrected = self.correct_spelling(text_lower)
        if was_corrected:
            if corrected in ["hello", "thanks", "bye", "exit"]:
                return corrected, was_corrected

        # Check topic map
        topics = self.topic_map.get(self.lang, self.topic_map["en"])
        if text_lower in topics:
            return topics[text_lower], was_corrected
        if corrected in topics:
            return topics[corrected], was_corrected

        return None, False

    def get_fact(self, topic):
        if topic not in self.shown_facts:
            self.shown_facts[topic] = set()

        facts = self.knowledge[self.lang].get(topic, [])
        available = [i for i in range(len(facts)) if i not in self.shown_facts[topic]]

        if not available:
            return None

        idx = random.choice(available)
        self.shown_facts[topic].add(idx)
        return facts[idx], len(available) - 1

    def display_fact(self, fact, remaining):
        r = self.responses[self.lang]
        print(f"\n🤖 ")
        print(f"💡 {fact['title']}")
        print(f"\n{fact['fact']}")
        print(f"\n🎯 {r.get('ask_more', '').split('\n')[0] if 'Example' not in fact['example'] else 'Example:'}")
        print(f"{fact['example']}")
        print(f"\n🔧 Application:")
        print(f"{fact['application']}")

        if remaining > 0:
            print(f"\n📚 {self.get_response('facts_remaining', remaining=remaining, topic=fact['title'])}")
        else:
            print(f"\n✅ {self.get_response('no_more_facts', topic=fact['title'])}")

    def handle_greeting(self):
        print(f"\n{self.get_response('greetings')}")

    def handle_thanks(self):
        print(f"\n🤖 {self.get_response('thanks')}")

    def handle_goodbye(self):
        print(f"\n🤖 {self.get_response('goodbye')}")

    def run(self):
        # Header
        print("=" * 50)
        print("           HAYDRBOT PRO v2.0")
        print("=" * 50)

        # Language selection
        while True:
            print("\nPlease select your language / اختر لغتك:")
            print("1. English")
            print("2. العربية (Arabic)")
            choice = input("\nEnter your choice (1 or 2) / اكتب رقمك (1 أو 2): ").strip()

            if self.set_language(choice):
                break
            print("\n❌ Invalid choice / اختيار غير صالح. Please try again / رجاءً جرب مرة تانية.")

        # Welcome
        print("\n" + "=" * 50)
        if self.lang == "ar":
            print("  أهلاً! أنا HaydrBot، صديقك الذكي.")
        else:
            print("  Hello! I am HaydrBot, your smart companion.")
        print("=" * 50)

        # Get name
        name = input(f"\n{self.get_response('name_prompt')}").strip()
        self.user_name = name if name else "Friend"
        print(f"\n🤖 {self.get_response('name_response', name=self.user_name)}")

        # Main loop
        while True:
            user_input = input(self.get_response("topic_prompt")).strip().lower()

            if not user_input:
                print(f"\n🤖 {self.get_response('invalid_input')}")
                continue

            # Check for exit
            if user_input in ["exit", "quit", "bye", "goodbye", "خروج", "باي", "مع السلامة"]:
                self.handle_goodbye()
                break

            # Check for greetings
            if user_input in ["hello", "hi", "hey", "greetings", "مرحبا", "اهلا", "هلا"]:
                self.handle_greeting()
                continue

            # Check for thanks
            if user_input in ["thanks", "thank you", "thx", "شكرا", "يسلمو", "تسلم"]:
                self.handle_thanks()
                continue

            # Detect topic
            topic, was_corrected = self.detect_topic(user_input)

            if topic and topic not in ["hello", "thanks", "bye", "exit"]:
                if was_corrected:
                    print(f"\n🤖 {self.get_response('spell_corrected', corrected=topic)}")

                result = self.get_fact(topic)
                if result:
                    fact, remaining = result
                    self.display_fact(fact, remaining)
                else:
                    print(f"\n🤖 {self.get_response('no_more_facts', topic=topic)}")
            else:
                print(f"\n🤖 {self.get_response('unknown')}")
                print(f"\n{self.get_response('topic_prompt')}")

if __name__ == "__main__":
    bot = HaydrBot()
    bot.run()
