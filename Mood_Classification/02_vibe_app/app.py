
# Import require files
import torch
import gradio as gr
import random

from typing import Dict
from transformers import pipeline

# Define model path
model_path = "Sairii/mood_classifier_distilbert"

# Define vibe map
vibe_map = {
    "sad": {
        "playlists": [
            "https://open.spotify.com/playlist/5DVUEqRL1EV8I9n65eBaAw?si=73e861e180b34945",
            "https://open.spotify.com/playlist/6yYA6aUGp8qUTgQWWYkPkP?si=4f18ea62db574b89",
            "https://open.spotify.com/playlist/2ZnAWYy4AOs8tpRUCGF6Py?si=fdc856b767e84fd1",
            "https://open.spotify.com/playlist/5tXGgf59I0CYYLSKoXyj55?si=0aaf98afaee544f9"
        ],
        "memes":[
            "https://images3.memedroid.com/images/UPLOADED24/6422c709a474e.webp",
            "https://cdn.verbub.com/images/cuando-estas-triste-y-escuchas-musica-triste-para-estar-mas-triste-219947.jpg",
            "https://cdn.memegenerator.es/imagenes/memes/full/29/24/29241765.jpg",
            "https://cdn.verbub.com/images/cuando-comes-porque-estas-triste-pero-ahora-estas-gordo-y-triste-66630.jpg",
            "https://www.thehealthy.com/wp-content/uploads/2020/10/xp1iwnvph2q51.jpg?fit=700,700",
            "https://i.pinimg.com/736x/26/40/87/2640871a50c7c0332fabffb040f409f7.jpg",
            "https://www.digitalmomblog.com/wp-content/uploads/2023/02/crying-behind-mask-meme.jpg",

       ],
       "images": [
           "https://getwallpapers.com/wallpaper/full/e/a/f/1186903-beautiful-cutest-wallpapers-in-the-world-1920x1200-phone.jpg",
           "https://i.pinimg.com/originals/c7/b9/62/c7b962b8330ec841278c07718532983b.jpg",
           "https://3.bp.blogspot.com/-nFQxBSDULZQ/WPFBNB-HAQI/AAAAAAAAAac/9AVttSP7mNwRA_oYA-SQydRt-4EXxsUvwCLcB/s1200/Excelentes-Frases-Para-Animar-A-Un-Amigo-Consejos-gratis.jpg",
           "https://4.bp.blogspot.com/-DhogjKFhjSA/VGJDQS7NgiI/AAAAAAAASaU/Gq7BwZjlpT4/s1600/postales-de-cachorros.jpg",
           "https://4.bp.blogspot.com/-iHbIEnMI5iQ/T5jgKqqwOJI/AAAAAAAAPPQ/52xa0v15EJ8/s1600/1+gatos+y+gatitos+hermosos,+tiernos+(10).jpg",

       ],
        "quotes":[
            "There is no greater sorrow than to recall happiness in times of misery.Dante Alighieri",
            "Life is made of so many partings welded together. Charles Dickens",
            "There are moments when I wish I could roll back the clock and take all the sadness away, but I have the feeling that if I did, the joy would be gone as well. –Nicholas Sparks",
            "Some stories don’t have happy endings. Even love stories. Maybe especially love stories. - Kristin Hannah, The Nightingale",
            "There is no greater sorrow than to recall, in misery, the time when we were happy. –Dante AligherI",
            "We must understand that sadness is an ocean, and sometimes we drown, while other days we are forced to swim. -R.M. Drake",
            "Heavy hearts, like heavy clouds in the sky, are best relieved by the letting of a little water. –Christopher Morley"
        ],
        "self_care": [
            "Take time to pause. Go outside and watch the clouds",
            "Reflect on a positive memory from the past week. Positivity boosts serotonin, a neurotransmitter associated with happiness",
            "Try coloring books or doodling. Artistic activities activate the brain’s relaxation pathways",
            "Drink some water.",
            "Go for a walk, even if it’s just around the room.",
            "Dance like no one is watching you"

        ],
        "affirmations": [
            "This sadness will pass, and brighter moments are ahead.",
            "You are taking things one breath at a time.",
            "You are strong enough to feel this, and you are resilient.",
            "You are surrounded by quiet support, even if you can't see it right now.",
            "Healing is happening, gently and slowly.",
            "You are allowed to rest and be kind to myself."
        ]
    },
    "angry":{
        "playlists":[
            "https://open.spotify.com/playlist/609gQW5ztNwAkKnoZplkao?si=fa8033175c4e410e",
            "https://open.spotify.com/playlist/37i9dQZF1EIhuCNl2WSFYd?si=115efc71faf94048",
            "https://open.spotify.com/playlist/5VP7RwPQ0xzCn0Y6588GTw?si=1fe3193a37a04090",
            "https://open.spotify.com/playlist/0Y0haVAr5i8ZBnc67G6oCl?si=36b33db7df654384"

        ],
        "memes":[
            "https://www.happierhuman.com/wp-content/uploads/2022/06/anger-meme-sayingimages-real-friends-ftm.jpg",
            "https://www.happierhuman.com/wp-content/uploads/2022/06/anger-meme-collegetimes-ill-stay-angry-instead.png",
            "https://i.imgflip.com/7diog0.jpg",
            "https://sayingimages.com/wp-content/uploads/angry-management-memes.jpg",
            "https://sayingimages.com/wp-content/uploads/angry-happiness-challenged-memes.jpg",
            "https://sayingimages.com/wp-content/uploads/angry-meme.jpg",
            "https://memecentral.org/wp-content/uploads/2019/08/angry-man-meme.jpg",
            "https://memecentral.org/wp-content/uploads/2019/08/angry-cat-noises-meme.jpg"

        ],
        "images":[
            "https://wallpapercave.com/wp/6GcHLY2.jpg",
            "https://burst.shopifycdn.com/photos/green-eyed-kitten.jpg?width=746&format=pjpg&exif=0&iptc=0",
            "https://wallpapercave.com/wp/QGsncry.jpg",
            "https://wallpaperaccess.com/full/276172.jpg",
            "https://cdn.wallpapersafari.com/1/56/MRJ3uA.jpg"

        ],
        "quotes":[
            "Anger makes you smaller, while forgiveness forces you to grow beyond what you were — Cherie Carter-Scott",
            "Anger is never without a reason, but seldom a good one. — Benjamin Franklin",
            "A fool gives full vent to his anger, but a wise man keeps himself under control — Proverbs 29:11",
            "When angry count to ten before you speak. If very angry, count to one hundred. - Thomas Jefferson",
            "The truth will set you free, but first it will piss you off.",
            "“Most misunderstandings in the world could be avoided if people would simply take the time to ask, What else could this mean?",
            "Speak when you are angry – and you will make the best speech you’ll ever regret. — Laurence J. Peter"

        ],
        "self_care":[
            "Take breaks from social commitments when overwhelmed",
            "Use mindfulness or meditation to center yourself",
            "Take a hot shower or bath with some music and candles",
            "Walk way and cold down",
            "Grab a paper and write about what's bugging you",
            "Count to 20 (or 50 or 34587 or more)"

        ],
        "affirmations":[
            "Your anger is a signal. Listen to what it’s trying to protect.",
            "It’s okay to feel this. Let it move through you, not control you.",
            "You don’t owe anyone your silence when something hurts.",
             "You’re not ‘too much’—they’re just not used to boundaries.",
            "Burning bridges? Babe, sometimes it’s called clearing dead weight.",
            "Pop off if you must—but make it poetic and powerful.",
            "Alright, you're feeling a bit blue, huh? Snap out of it... gently, of course."
        ]
    },
    "anxious":{
        "playlists":[
            "https://open.spotify.com/playlist/1r4hnyOWexSvylLokn2hUa?si=581df210bc144a17",
            "https://open.spotify.com/playlist/7JabddFr3Q6JPsND4v9Swf?si=ec9ea7bbab86403b",
            "https://open.spotify.com/playlist/18L9Oembkvoo7ciwrUDGAi?si=ca0bd53022bb4ab3",
            "https://open.spotify.com/playlist/5z5prxfyNclz9U3bE1YIZo?si=41d9c06a714c4707"
        ],
        "memes":[
            "https://www.happierhuman.com/wp-content/uploads/2022/03/memes-anxiety-instagram-what-if-it-does.jpg",
            "https://www.happierhuman.com/wp-content/uploads/2022/03/memes-anxiety-realvitamins-where-do-i-begin.jpg",
            "https://www.happierhuman.com/wp-content/uploads/2022/03/memes-anxiety-realvitamins-panic-attacks-activated.jpg",
            "https://www.happierhuman.com/wp-content/uploads/2022/03/memes-anxiety-realvitamins-mom-do-you-even-know-me.jpg",
            "https://ruinmyweek.com/wp-content/uploads/2020/01/anxiety-memes-2.png",
            "https://starecat.com/content/wp-content/uploads/when-someone-says-dont-be-anxious-and-your-anxiety-is-cured.jpg",
            "https://i.pinimg.com/originals/89/69/b2/8969b2f3ec5fdd0ccaf331262f8287e3.jpg"

        ],
        "images":[
            "https://www.pixelstalk.net/wp-content/uploads/2016/07/Relaxing-Photos-HD.jpg",
            "https://getwallpapers.com/wallpaper/full/8/8/9/1498083-mind-relaxing-wallpapers-1920x1080-tablet.jpg",
            "https://wallpaperaccess.com/full/3815908.jpg",
            "https://i.pinimg.com/originals/d9/af/a3/d9afa330a7b89865db34e645c86a36ce.jpg",
            "https://blog.uptodown.com/wp-content/uploads/relax-app-android-featured.jpg.webp",
            "https://db5vrvzqvdahe.cloudfront.net/wp-content/uploads/shutterstock_435387934.jpg",
            "https://st2.depositphotos.com/1146092/11636/i/950/depositphotos_116368986-stock-photo-relax-spa-wellness-dog.jpg"

        ],
        "quotes":[
            "“No need to hurry. No need to sparkle. No need to be anybody but oneself.” — Virginia Woolf",
            " “Anxiety happens when you think you have to figure everything out all at once. Breathe. You’re strong. You got this.” — Karen Salmansohn",
            " “If you want to test your memory, try to recall what you were worrying about one year ago today.” — E. Joseph Cossman",
            " “Feel the fear and do it anyway.” — Susan Jeffers",
            "“Sometimes letting go is the best way to find peace.” — Donna Goddard",
            "It’s okay to not be okay. Just don’t stay that way.",
            "“Breathe. Let go. And remind yourself that this very moment is the only one you know you have for sure.” — Oprah Winfrey",
            "“You don’t have to have it all figured out to move forward.” — Roy T. Bennett"

        ],
        "self_care":[
            "Dance to your favorite songes",
            "Do something active: go for a walk, go to the gym",
            "Call or text a loved one",
            "Cozy up in your favorite spot",
            "Watch a movie or a tv show",
            "Clean up your bedroom",


        ],
        "affirmations":[
            "You are safe in this moment. Breathe through it.",
            "This fear will pass. You’ve survived every wave so far.",
            "You don’t need to fix everything right now. Just be here.",
            "It's okay for your mind to race right now. You are safe.",
            "This feeling of anxiety is temporary, and it will pass.",
            "Worries are just thoughts in fancy, annoying costumes. See 'em, then ignore 'em.",
            "Yeah, your body's on high alert. Tell it to take a coffee break, you've got this.",
            "You've survived worse, trust me. This is just a plot twist, not the grand finale.",
            "So what if you're a mess? Even masterpieces start with a bit of chaos, right?"

        ]
    },
    "joy":{
        "playlists":[
            "https://open.spotify.com/playlist/37i9dQZF1DXdPec7aLTmlC?si=c1e32eeb15734773",
            "https://open.spotify.com/playlist/37i9dQZF1EIgG2NEOhqsD7?si=6e44ed2babe24541",
            "https://open.spotify.com/playlist/0faAJkECam6JhkR9TLolIQ?si=aacb24457354433b",
            "https://open.spotify.com/playlist/6hXwzaSaiiWUazPjpQn0Yl?si=d4da8cb30cf84d49"

        ],
        "memes":[
            "https://i.pinimg.com/originals/97/79/88/977988c0c50650833040e74b03b3d148.jpg",
            "https://i.pinimg.com/originals/ba/fb/5d/bafb5de2a3e9b7e7f246e89385b30a6f.jpg",
            "https://img.izismile.com/img/img15/20231218/640/joyful_animal_humor_memes_and_pics_spreading_smiles_640_high_18.jpg",
            "https://www.musicraiser.net/wp-content/uploads/2020/01/31-Joyful-Memes-to-Make-You-Smile-Whole-Day-18-545x495.jpg",
            "https://sayingimages.com/wp-content/uploads/dont-worry-you-got-this-motivational-memes.jpg",
            "https://sayingimages.com/wp-content/uploads/motivational-today-is-the-day-memes.jpg"

        ],
        "images":[
            "https://www.success.com/wp-content/uploads/legacy/sites/default/files/2_29.jpg",
            "https://3.bp.blogspot.com/-lf1l7-_tVr8/WcDydIUsnUI/AAAAAAAAbZ0/k81Qn_guYlwhrcwDH8aZ7CJ1yvXPnJ0pwCLcBGAs/s1600/You%2Bcome%2Bso%2Bfar2.png",
            "https://sayingimages.com/wp-content/uploads/be-the-best-you-can-be-motivational-memes.jpg",
            "https://sayingimages.com/wp-content/uploads/whos-awesome-youre-awesome-motivational-memes.jpg",
            "https://sayingimages.com/wp-content/uploads/motivational-youre-awesome-memes.jpg.webp"
            

        ],
        "quotes":[
            "“They say a person needs just three things to be truly happy in this world: someone to love, something to do, and something to hope for.”― Tom Bodett",
            "Focus on the journey, not the destination. Joy is found not in finishing an activity but in doing it. - Greg Anderson",
            "If the sight of the blue skies fills you with joy, if a blade of grass springing up in the fields has power to move you, if the simple things of nature have a message that you understand, rejoice, for your soul is alive. - Eleonora Duse",
            "The sun does not shine for a few trees and flowers, but for the wide world's joy. Henry Ward Beecher",
            "Let your joy be in your journey - not in some distant goal. - Tim Cook",
            "“When we are centered in joy, we attain our wisdom.” —Marianne Williamson"

        ],
        "self_care":[
            "Go watch the sunset",
            "Treat yourself to an amazing dessert",
            "Treat yourself & a friend to coffe at a cute cae",
            "Take yourself out for lunch",
            "Look at the stars",
            "Dance & sing to your favorite song"

        ],
        "affirmations":[
            "Yeah, you're basically a **joy magnet**. Don't act surprised, you earned it.",
            "Turns out, **happiness looks great on you**. Keep it up, buttercup.",
            "Laughter's your new superpower, and you're wielding it like a **pro**.",
            "**Unapologetically gleeful**, that's you. And honestly? It's a look.",
            "Go on, spread that **contagious cheer**. The world could use a dose of your fabulousness.",
            "You find delight in the simple pleasures and beauty all around you.",
            "You are worthy of abundant joy, and it is your natural state.",
            "Laughter comes easily to you, brightening your day and those around you.",
            "You are alive, vibrant, and bursting with positive energy.",
            "Joy multiplies within you as you share your light with the world."


        ]
    },
    "tired":{
        "playlists":[
            "https://open.spotify.com/playlist/37i9dQZF1EIcUQK8Nwn2jv?si=5e7ae3e1dcb745a8",
            "https://open.spotify.com/playlist/4l1BhoNigXILxeQQeBDbvg?si=e1ab5c466bf14eca",
            "https://open.spotify.com/playlist/6rjP6aBpLGgr5odndfARlq?si=d8a4e7ff9d374497",
            "https://open.spotify.com/playlist/7MUhmEs5iduvuWid91mnw6?si=553213fcd7b94638"

        ],
        "memes":[
            "https://www.digitalmomblog.com/wp-content/uploads/2023/09/funny-tired-meme.jpg.webp",
            "https://www.digitalmomblog.com/wp-content/uploads/2023/09/tired-meme-funny.jpeg.webp",
            "https://inspirationfeed.com/wp-content/uploads/2020/07/Tired-Meme19.jpg",
            "https://inspirationfeed.com/wp-content/uploads/2020/07/Tired-Meme33.jpg",
            "https://piximus.net/media2/55735/tired-memes-10.jpg",
            "https://i.pinimg.com/originals/83/f4/01/83f4016f7e3671275f78b5d7562e19f3.jpg"

        ],
        "images":[
            "https://quotefancy.com/media/wallpaper/3840x2160/7390377-Carlos-Wallace-Quote-When-you-are-tired-you-rest-You-don-t-give-up.jpg",
            "https://cdn3.careeraddict.com/uploads/article/60864/tips-to-wake-up-infographic.png",
            "https://www.verywellhealth.com/thmb/ZncipGImtDmdZ4xECfzo1dd9y10=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/reasons-for-poor-sleep-quality-45881701-52c54387761c4baa9f702e8a5f86b9a7.gif",
            "https://my.clevelandclinic.org/-/scassets/images/org/health/articles/12119-insomnia",
            "https://www.awesomeinventions.com/wp-content/uploads/2016/02/Tired-Just-Tired.jpg"


        ],
        "quotes":[
            "You can do anything but not everything - David Allen",
            "Silence doesn't always mean yes. Sometimes, it means, I am tired of explaining to people who don't even care to understand",
            "“Tired minds don’t plan well. Sleep first, plan later.” – Walter Reisch",
            "“Even the darkest night will end and the sun will rise.” – Victor Hugo",
            "“Even heroes need a break.” – Stan Lee",
            "Sometimes I wish I could just press pause and catch my breath."

        ],
        "self_care":[
            "Take a nap with no alarm",
            "Take something off of your to-do list",
            "Say no to something",
            "Watch your favorite TV show",
            "Use a weighted blanket",
            "Put your phone on Do Not Disturb"

        ],
        "affirmations":[
            "You're not lazy, you're in **energy-saving mode**. Smart, really.",
            "Operation Recharge is a go! Prepare for maximum horizontal time.",
            "Conquering the world can wait. Your couch, however, cannot.",
            "You're done. D-O-N-E. Now go get that beauty sleep, you earned it.",
            "Rest isn’t lazy—it’s necessary.",
            "You don’t have to do it all. You just have to breathe.",
            "Your body and soul are asking for care. Listen.",
            "It's okay to feel tired. You've done enough for today.",
            "Your body is asking for rest, and you are listening.",

        ]

    },
    "numb":{
        "playlists":[
            "https://open.spotify.com/playlist/7DtC8X9lVC5VulFqTZARQA?si=9f533b357b5f4696",
            "https://open.spotify.com/playlist/6kR2MtMOkP0CRZYRbbjLCB?si=dabbb4e18ef94831",
            "https://open.spotify.com/playlist/04hyzNf9DUjOPkI7v7nDoC?si=01fb238ef4a943ef",
            "https://open.spotify.com/playlist/1wU8Bso3aX6ophkPYvETs9?si=28f126326bf94bf0"

        ],
        "memes":[
            "https://i.imgflip.com/77ft0w.jpg",
            "https://themighty.com/wp-content/uploads/2019/11/via-QuickMeme.jpg",
            "https://themighty.com/wp-content/uploads/2019/11/Quickmemee.jpg",
            "https://i.pinimg.com/originals/82/cb/00/82cb002d89fabe4e2c49fcaf25434eb7.png",
            "https://www.reddit.com/media?url=https%3A%2F%2Fi.redd.it%2F7mjxeq54mzb31.jpg",
            "https://i.pinimg.com/originals/fa/95/94/fa9594debda1e02ca8bb8b84e9f3ec0a.png"

        ],
        "images":[
            "https://www.maestronews.com/wallpapers/landscape/sunrise/sunrise_10.jpg",
            "https://www.pixelstalk.net/wp-content/uploads/2016/08/Night-Sky-Milky-Way-Galaxy-Wallpaper.jpg",
            "https://www.pixelstalk.net/wp-content/uploads/2016/03/Cute-Animal-Wallpaper-HD-desktop.jpg",
            "https://cdn.pixabay.com/photo/2017/05/18/13/46/rainbow-2323708_1280.jpg",
            "https://www.factinate.com/wp-content/uploads/2018/07/baby-animals.jpg"

        ],
        "quotes":[
            "“I just let the pain take over, allowing it to numb the pain of being left behind.” ― Jessica Sorensen, The Coincidence of Callie & Kayden",
            "“I’ve perfected the art of the fake smile. It’s not so difficult when you are completely numb.” ― Bethany Griffin, Masque of the Red Death",
            "“I should have been angry, but I was struggling to feel much of anything.” ― Karie Fugett, Alive Day: A Memoir",
            "“Better to feel nothing, to be numb, than to lose control. It's the only way I know to deal with it.” ― Julie Kagawa, The Forever Song",
            "“Some scars don’t hurt. Some scars are numb. Some scars rid you of the capacity to feel anything ever again.” ― Joyce Rachelle",
            "“I thought I’m healing but the truth is, I just stopped feeling.” – C. C. Aurel"

        ],
        "self_care":[
            "Try 5 minutes of journaling, doesn't need to be perfect, just pour those thoughts somewhere",
            "Give yourself permission to feel exactly how you are feeling",
            "Connect with others at your own pace: have a small conversation with a friend",
            "Rest and don't feel guilty about it",
            "Go for a walk and listen to the sounds around you",
            "Do breathing exercises:Try inhaling for four counts, holding for four, and exhaling for four (the 4-4-4 method) "

        ],
        "affirmations":[
            "If your heart’s on airplane mode, fine—but don’t crash.",
            "You’re still a whole damn person, even when you feel nothing.",
            "Frozen doesn’t mean gone. You’ll thaw. Slowly. And dramatically.",
            "Okay, emotions took a vacation, huh? Fine, you do you.",
            "Healing is happening, even when it feels like nothing is happening.",
            "You are supported, even if you can't feel it right now.",
            "Be kind to yourself in this space of emotional quiet.",
            "You are whole, even in this moment of numbness."

        ]
    },
    "confident":{
        "playlists":[
            "https://open.spotify.com/playlist/37i9dQZF1EIhAa4OzjmrFk?si=6a513706c2634f18",
            "https://open.spotify.com/playlist/5QK5DcACsK2r9VzNwSgHl4?si=2a6efce45370425e",
            "https://open.spotify.com/playlist/37i9dQZF1DX4fpCWaHOned?si=ec97e651466c4311",
            "https://open.spotify.com/playlist/2f67AbWKCd2Ry2jkzDejs7?si=5fe719ef827b4d39"

        ],
        "memes":[
            "https://i.imgflip.com/1ks1mm.jpg",
            "https://imgix.bustle.com/2017/1/17/7ed6d773-dfd1-4fd6-87eb-713114b0102c.jpg?w=414&h=600&fit=crop&crop=faces&auto=format%2Ccompress&q=50&dpr=2",
            "https://i.imgflip.com/1e4msy.jpg",
            "https://i.imgflip.com/1ntulb.jpg",
            "https://i.pinimg.com/originals/bc/2e/65/bc2e653597ba3cdab4dd7dbc40b90b21.jpg",
            "https://sayingimages.com/wp-content/uploads/hold-my-beer-i-got-this-meme.jpeg"

        ],
        "images":[
            "https://sayingimages.com/wp-content/uploads/motivational-arise-go-forth-and-conquer-memes.jpg",
            "https://cdn.pixabay.com/photo/2015/09/24/06/09/positive-954797_1280.jpg",
            "https://images.huffingtonpost.com/2015-12-04-1449210149-2724155-SelfConfidence.png",
            "https://bethlehemdenver.com/wp-content/uploads/2020/07/FINISH-LINE.jpg",
            "https://cdn.pixabay.com/photo/2024/05/24/12/58/ai-generated-8785023_1280.png"

        ],
        "quotes":[
            "“Be who you are and say what you feel, because those who mind don't matter, and those who matter don't mind.” ― Bernard M. Baruch",
            "“You probably wouldn’t worry about what people think of you if you could know how seldom they do.” ― Olin Miller",
            "“Do not fear to be eccentric in opinion, for every opinion now accepted was once eccentric.” ― Bertrand Russell",
            "“Believe in your infinite potential. Your only limitations are those you set upon yourself.” ― Roy T. Bennett, The Light in the Heart",
            "“Accept who you are; and revel in it.” ― Mitch Albom, Tuesdays with Morrie: An Old Man, a Young Man, and Life's Greatest Lesson",
            "No matter how old you are now. You are never too young or too old for success or going after what you want."

        ],
        "self_care":[
            "Surround yourself with positive people",
            "Take care of your body: diet, exercise, meditation",
            "Always be kind to yourself",
            "Practive positive self-talk",
            "Do things you are good at"
            

        ],
        "affirmations":[
            "You’re the whole damn meal. Stop acting like a side dish.",
            "Confidence looks good on you—don’t take it off for anyone.",
            "They should be grateful they even get to witness your glow.",
            "Oh, you thought you couldn't? Cute. Watch you **absolutely crush it**.",
            "You embrace your authentic self, knowing you are enough.",
            "You move through the world with quiet assurance and grace.",
            "Your presence is a gentle power that inspires those around you.",
            "You believe in yourself, and that belief softly guides your way.",
            "You are secure in who you are, finding peace in your own unique journey."


        ]
    },
    "hopeful":{
        "playlists":[
            "https://open.spotify.com/playlist/37i9dQZF1EIemCZWVgQTXB?si=a0546c750dff4601",
            "https://open.spotify.com/playlist/77qvKHsd1c9YGbGcnZVNzE?si=09f097151e444c26",
            "https://open.spotify.com/playlist/4ofywy1Z3LbiSTlmSLPR0s?si=585d1d45ce84454b",
            "https://open.spotify.com/playlist/754LgMDMRwGna2RvnfTePc?si=7186e2ecbda546bd"

        ],
        "memes":[
            "https://sayingimages.com/wp-content/uploads/theres-still-hope-meme-300x300.jpg",
            "https://sayingimages.com/wp-content/uploads/sometimes-you-have-to-tell-yourself-i-am-a-share-and-attack-the-day-hope-meme.jpg",
            "https://sayingimages.com/wp-content/uploads/you-always-have-hope-even-if-theres-not-a-chance-in-hell-meme.jpg",
            "https://i.pinimg.com/originals/46/d9/30/46d9309e7a040b9151531f2a8e87550b.jpg",
            "https://sheideas.com/wp-content/uploads/2018/10/funny-positive-meme-18-585x403.jpg",
            "https://www.kerryjheckman.com/uploads/7/2/8/1/72815985/published/when-someone-understands.jpg?1523282931"

        ],
        "images":[
            "https://library.neura.edu.au/wp-content/uploads/sites/3/2017/01/Hope.jpg",
            "https://centralofsuccess.com/wp-content/uploads/2018/03/Inspirational-Hope-Quotes.jpg",
            "https://www.thewowstyle.com/wp-content/uploads/2015/01/whe-the-world-says-give-up-hope-whispers-try-it-one-more-time.jpg",
            "https://www.wishesmsg.com/wp-content/uploads/Hope-messages-and-sayings.jpg",
            "https://i.pinimg.com/736x/db/a6/a6/dba6a688a2f2e3053b3b373b75ec3b7a.jpg"

        ],
        "quotes":[
            "“You may say I'm a dreamer, but I'm not the only one. I hope someday you'll join us. And the world will live as one.”― John Lennon",
            "“I like the night. Without the dark, we'd never see the stars.” ― Stephenie Meyer, Twilight",
            "“If you're reading this... Congratulations, you're alive. If that's not something to smile about, then I don't know what is.” ― Chad Sugg, Monsters Under Your Head",
            "“If pain must come, may it come quickly. Because I have a life to live, and I need to live it in the best way possible. If he has to make a choice, may he make it now. Then I will either wait for him or forget him.” ― Paulo Coelho, By the River Piedra I Sat Down and Wept",
            "“Never lose hope. Storms make people stronger and never last forever.” ― Roy T. Bennett, The Light in the Heart",
            "“It's amazing how a little tomorrow can make up for a whole lot of yesterday.” ― John Guare, Landscape of the Body"

        ],
        "self_care":[
            "Give yourself compliments",
            "Keep a goal journal",
            "Let loved ones lift you up",
            "Take time out to journal - writing your thoughts and feelings down in one place can be really empowering. It can also help to ‘declutter’ your busy mind",
            "Binge watch your favourite TV show or movies - set time aside to chill and do something you enjoy, whether that’s alone or with someone you love.",
            "Spend time outdoors - choose to re-connect with nature"

        ],
        "affirmations":[
            "Hope is your quiet rebellion. Keep it alive.",
            "Trust the seeds you’ve planted. Bloom is coming.",
            "You don’t have to know how—it’s okay to just believe.",
            "Even in the quiet, you feel a gentle stirring of possibility.",
            "Still got that fire in your belly? Good. It's leading you somewhere epic.",
            "Don't just hope for it, expect it. You're manifesting greatness, darling.",
            "Your future's looking so bright, you might need shades. Just sayin'.",
            "Time to turn up the optimism. Your vibe is attracting your tribe... and cool opportunities.",
            "Plot twist: everything's about to work out. You saw it here first.",

        ]
    }



}

classifier = pipeline(task = "text-classification",
              model = model_path,
              device = "cuda" if torch.cuda.is_available() else "cpu",
              top_k = 2,
              batch_size = 32)


# Define our function to use with our model
def mood_text_classifier(text:str):

  # Outputs from the pipeline
  outputs = classifier(text)[0]
  result = outputs[0]

  label = result["label"].lower()
  score = result["score"]

  #Vibe map
  vibe = vibe_map.get(label, {})
  playlist = random.choice(vibe.get("playlists", ["No playlist found"]))
  meme = random.choice(vibe.get("memes", ["No meme found"]))
  image = random.choice(vibe.get("images", ["No image found"]))
  quote = random.choice(vibe.get("quotes", ["No quote found"]))
  self_care = random.choice(vibe.get("self_care", ["No tip found"]))
  affirmation = random.choice(vibe.get("affirmations", ["No affirmation found"]))

  return{
      "emotion": label,
      "confidence":round(score, 3),
      "playlist": playlist,
      "meme": meme,
      "image": image,
      "quote": quote,
      "self_care": self_care,
      "affirmation": affirmation
      
  }

# Create the gradio interface
def mood_interface(text, selections):
    result = mood_text_classifier(text)
    summary_lines = [
        f"🧠 Emotion: {result['emotion'].capitalize()}",
        f"📈 Confidence: {round(result['confidence']*100, 2)}%"
    ]

    # Only add what the user picked
    playlist_html = ""
    if "Playlist" in selections:
       playlist_html = f'<a href="{result["playlist"]}" target="_blank">🎵 Listen to playlist</a>'
    if "Quote" in selections:
        summary_lines.append(f"✨ Quote: {result['quote']}")
    if "Self-care Tip" in selections:
        summary_lines.append(f"💡 Self-care Tip: {result['self_care']}")
    if "Affirmation" in selections:
        summary_lines.append(f"💬 Affirmation:\n{result['affirmation']}")

    summary = "\n".join(summary_lines)

    # For images, only show if picked, otherwise return None
    meme_url = result["meme"] if "Meme" in selections else None
    image_url = result["image"] if "Inspirational Image" in selections else None

    return summary, playlist_html, meme_url, image_url


demo = gr.Interface(
    fn=mood_interface,
    inputs=[
        gr.Textbox(lines=4, placeholder="Write your journal entry here...", label="How are you feeling today?"),
        gr.CheckboxGroup(
            ["Playlist", "Meme", "Inspirational Image", "Quote", "Self-care Tip", "Affirmation"],
            label = "What do you need today?",
            value = ["Affirmation"]
        )
    ],
    outputs=[
        gr.Textbox(label="Mood Summary"),
        gr.HTML(label="Playlist"),
        gr.Image(label="Meme"),
        gr.Image(label="Image")
        ],
    title="🧠 Mood Classifier with a vibe",
    description="Journal your heart out. Choose how you want to be loved today: playlists, memes, inspirational memes, self_care tips, or inspirational quotes."
)

# Launch the interface
if __name__ == "__main__":
  demo.launch()