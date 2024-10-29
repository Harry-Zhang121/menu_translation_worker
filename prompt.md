Role: You are a profesional multilingual translator.
Input: You will be given a mensa menu in German, in html format.
Task: 
    1. Some dishes may not be obvious right away for customers from English speaking world. List these dishes and write a short note to help them understand the dish by referencing their home cuisine.
        examples("Bratwurst":"Bratwurst is a type of German sausage made from pork, beef, or veal")
    2. Translate the menu into English. Focus on the accuracy of meaning. Do not translate word-by-word. Add your note to the menu where explanation is required.
Output: You should output the translated version using `markdown` format. Use heading and unordered list to make it easier to read.


---
Role: You are a professional German-Chinese translator.
Input: You will be given a mensa menu in German, in html format.
Task: 
    1. Some dishes may not be obvious right away for customers from Chinese speaking world. First list these dishes and write a short note to help them understand the dish by referencing their home cuisine.
        examples(\"Ravioli\":\"Ravioli 类似于中国的馄饨或饺子。馅料的种类可以是芝士、肉类或蔬菜等，配以番茄酱或奶油酱。\")
    2. Translate the menu into Chinese. Focus on the accuracy of meaning. Do not translate word-by-word. Add your note to the menu where explanation is required.
Output: You should output the translated version using `markdown` format. Use heading and unordered list to make it easier to read.

Below is the raw menu
```
\n                        \n                                                                                                                                                            <b>Menü 1</b><br />\n                                                                            Vegetarisches Gemüse und Cous-Cous mit Harissa (17,18,22,We) Bunter Rohkostsalat (9,Ei,La,Sf,We),  Mandarinenquark (La)<br />\n                                                                        <br/>\n                                                                                                                                                                                            <b>Menü 2</b><br />\n                                                                            KlimaTeller: Bratwurst (13) Ketchup,  Pommes Frites,  Alternativbeilage,  Bunt gemischter Blattsalat,  Klare Salatsoße (Sf),  Weiße Salatsoße Dressing (9,Ei,La,Sf,We),  Obst (Apfel aus biologischem Anbau)<br />\n                                                                        <br/>\n                                                                                                                                                                                            <b>Wahlessen</b><br />\n                                                                                                                        - &quot;Pommes mal anders&quot; Poutine Kanada Style (1,3,5,13,17,La,Sf,Sw,We,Ge),  Scharfes Tomaten-Topping (Sl,Sf)<br />\n                                                                                    - KlimaTeller: Vegan: Penne Rigate mit Tomaten (22,We) (Penne aus biologischem Anbau) <br />\n                                                                                    - Winterhilfe Saar: Unter Vorlage des Berechtigungsscheines erhalten Sie das Vegetarische Menü<br />\n                                                                                                                <br/>\n                                                                                                                                                                                            <b>Salatbuffet</b><br />\n                                                                            Salattheke: Tomatensalat Weisskraut,  Gurken,  Zwiebel Ringe,  Karotten,  Gemischter Paprika,  Mais,  Peperoni,  Chicoree, Lollo Bianco, Radicchio,  Klare Salatsoße (Sf), Weiße Salatsoße (9,Ei,La,Sf,We),  Kräuter, Hülsenfrüchte<br />\n                                                                        <br/>\n                                                                                                                                <b>Mensacafé Mittag</b><br />\n                                                                                                                        - Flammkuchen &quot;Elsässer Art&quot; (2,3,13,La,We) <br />\n                                                                                    - Flammkuchen &quot;Mediteran&quot; (La,We) <br />\n                                                                                                                <br/>\n                                                                                                                                                \n     
```

## one line version

```
Input: You will be given a mensa menu in German, in html format.\nTask: \n    1. Some dishes may not be obvious right away for customers from English speaking world. List these dishes and write a short note to help them understand the dish by referencing their home cuisine.\n        examples(\"Bratwurst\":\"Bratwurst is a type of German sausage made from pork, beef, or veal\")\n    2. Translate the menu into English. Focus on the accuracy of meaning. Do not translate word-by-word. Add your note to the menu where explanation is required.\nOutput: You should output the translated version using `markdown` format. Use heading and unordered list to make it easier to read.\n\n\n---\nRole: You are a professional German-Chinese translator.\nInput: You will be given a mensa menu in German, in html format.\nTask: \n    1. Some dishes may not be obvious right away for customers from Chinese speaking world. First list these dishes and write a short note to help them understand the dish by referencing their home cuisine.\n        examples(\\\"Ravioli\\\":\\\"Ravioli 类似于中国的馄饨或饺子。馅料的种类可以是芝士、肉类或蔬菜等，配以番茄酱或奶油酱。\\\")\n    2. Translate the menu into Chinese. Focus on the accuracy of meaning. Do not translate word-by-word. Add your note to the menu where explanation is required.\nOutput: You should output the translated version using `markdown` format. Use heading and unordered list to make it easier to read.\n\nBelow is the raw menu\n```\n\\n                        \\n                                                                                                                                                            <b>Menü 1</b><br />\\n                                                                            Vegetarisches Gemüse und Cous-Cous mit Harissa (17,18,22,We) Bunter Rohkostsalat (9,Ei,La,Sf,We),  Mandarinenquark (La)<br />\\n                                                                        <br/>\\n                                                                                                                                                                                            <b>Menü 2</b><br />\\n                                                                            KlimaTeller: Bratwurst (13) Ketchup,  Pommes Frites,  Alternativbeilage,  Bunt gemischter Blattsalat,  Klare Salatsoße (Sf),  Weiße Salatsoße Dressing (9,Ei,La,Sf,We),  Obst (Apfel aus biologischem Anbau)<br />\\n                                                                        <br/>\\n                                                                                                                                                                                            <b>Wahlessen</b><br />\\n                                                                                                                        - &quot;Pommes mal anders&quot; Poutine Kanada Style (1,3,5,13,17,La,Sf,Sw,We,Ge),  Scharfes Tomaten-Topping (Sl,Sf)<br />\\n                                                                                    - KlimaTeller: Vegan: Penne Rigate mit Tomaten (22,We) (Penne aus biologischem Anbau) <br />\\n                                                                                    - Winterhilfe Saar: Unter Vorlage des Berechtigungsscheines erhalten Sie das Vegetarische Menü<br />\\n                                                                                                                <br/>\\n                                                                                                                                                                                            <b>Salatbuffet</b><br />\\n                                                                            Salattheke: Tomatensalat Weisskraut,  Gurken,  Zwiebel Ringe,  Karotten,  Gemischter Paprika,  Mais,  Peperoni,  Chicoree, Lollo Bianco, Radicchio,  Klare Salatsoße (Sf), Weiße Salatsoße (9,Ei,La,Sf,We),  Kräuter, Hülsenfrüchte<br />\\n                                                                        <br/>\\n                                                                                                                                <b>Mensacafé Mittag</b><br />\\n                                                                                                                        - Flammkuchen &quot;Elsässer Art&quot; (2,3,13,La,We) <br />\\n                                                                                    - Flammkuchen &quot;Mediteran&quot; (La,We) <br />\\n                                                                                                                <br/>\\n                                                                                                                                                \\n     \n```\n
```


## 菜单翻译与解释

### 可能不熟悉的菜肴
- **Bratwurst:** 一种德国香肠，通常由猪肉、牛肉或小牛肉制成。
- **Poutine:** 加拿大的一种特色美食，类似于中国的“手抓饼”或“煎饼”，上面加有肉汁和奶酪块。
- **Flammkuchen (Elsässer Art):** 类似于披萨，但面皮更薄，上面常加培根、洋葱和奶油。
- **Flammkuchen (Mediteran):** 类似披萨的薄脆饼，上面配有地中海风味的配料，如橄榄和番茄。

### 菜单翻译

#### 菜单1
- **素菜和粗麦粉配哈利萨辣酱** (Vegetarisches Gemüse und Cous-Cous mit Harissa)
  - 色拉：彩色生蔬色拉 (Bunter Rohkostsalat)
  - 甜点：橘子味奶酪 (Mandarinenquark)

#### 菜单2
- **气候友好餐** (KlimaTeller): 
  - Bratwurst 德国香肠
  - 番茄酱
  - 炸薯条
  - 其他选择的配菜
  - 混合色拉
  - 透明色拉酱 (Klare Salatsoße)
  - 白色色拉酱 (Weiße Salatsoße)
  - 水果 (如有机苹果)

#### 自选餐
- **“另类薯条”加拿大风 Poutine:**
  - 辣番茄浇头 (Scharfes Tomaten-Topping)
- **气候友好餐: 纯素：有机番茄意大利面 (Penne Rigate mit Tomaten)**
- **萨尔冬季救济:** 提供有效证件可获取素食餐

#### 沙拉自助餐
- **色拉吧:** 
  - 番茄色拉
  - 白甘蓝、黄瓜、洋葱圈、胡萝卜、混合椒类、玉米、辣椒、菊苣、绿叶莴苣、紫叶莴苣
  - 透明色拉酱
  - 白色色拉酱
  - 香草调料
  - 豆类

#### Mensacafé 午餐
- **法兰饼“阿尔萨斯风”** (Flammkuchen "Elsässer Art")
- **法兰饼“地中海风”** (Flammkuchen "Mediteran")"