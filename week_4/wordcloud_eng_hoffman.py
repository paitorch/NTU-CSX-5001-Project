# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 20:11:34 2018

@author: purav
"""

from wordcloud import WordCloud
import matplotlib.pyplot as plt
import jieba


demo_text = '''
Pediatricians to lobby Congress for gun control laws 350 pediatricians will head to Capitol Hill Tuesday to lobby in favor of gun violence legislation, including two Senate bills.
Young victims of gun violence, including students from Marjory Stoneman Douglas High School, stand together on stage at the conclusion of the March for Our Lives rally on March 24, 2018 in Washington.Chip Somodevilla / Getty Images file
Dr. Ben Hoffman will never forget the three-year-old who came into the emergency room with a gunshot wound.
“The child had shot himself in the face. It was obvious that was going to be a deadly injury,” Hoffman recalled. Members of the American Psychological Association at the "March For Our Lives" gun violence rally held in Washington, D.C. on March 24, 2018. Physician and other health provider groups say gun violence and gun control are matters of public health. Maggie Fox / NBC News
“We were trying to resuscitate him. We were trying to see if we could get anything back.”But the devastation that a gun can wreak on the tiny head of a toddler is too much. The child died.
“Those are the kinds of things you can’t forget. It haunts me to this day,” said Hoffman, who is now chair of the American Academy of Pediatrics’ Council on Injury, Violence and Poison Prevention.
“I remember the parents in tears. I remember being in tears.”
Hoffman and 350 colleagues will bring this and other stories to Congress Tuesday as part of a day spent lobbying in favor of gun legislation.
1,300 kids killed by guns each year
They’re supporting a proposed assault weapons ban sponsored by senate Democrats and a bipartisan Senate bill that would restrict the sale of semiautomatic weapons to people 21 and older.
The pediatrics group has been outspoken on the issue of gun violence for years, but Hoffman said this year may offer a special opportunity to get federal legislation.
“This is a unique time,” Hoffman said.
“The events of the last several months, most notably the shooting at Parkland, has helped elevate the issue and has helped spark conversations.”
“Pediatricians will have three main messages for their federal legislators,” the AAP said. Their requests:
Provide $50 million to the Centers for Disease Control and Prevention (CDC) for public health research into firearm safety and injury prevention;
Support a minimum purchase age of 21 for semiautomatic assault weapons and high-capacity magazines; and
Support a ban on semiautomatic assault weapons.
“This is about protecting children from the impact of gun-related injuries,” said Hoffman, who practices at Oregon Health and Science University​.
The AAP says pediatricians should be seen as honest brokers in the debate over gun violence.
Related
Kids walk out of school to protest against gun violence
“We can all agree that children should never be injured by a gun. As a pediatrician, what I care about more than anything else is making sure that kids are safe and healthy,” Hoffman said.
The Academy urges pediatricians to ask about guns in the home.
“Ask about the presence of firearms in the home, and counsel parents who do keep guns to store them unloaded in a locked case, with the ammunition locked separately,” it advises its members.
“While the safest home for children is one without a gun, safe storage practices can significantly reduce the risk of gun injury or death.”
The National Rifle Association and supporters have fought back against these advisories, sponsoring legislation to stop pediatricians from asking parents about guns in the home — something that really puzzles doctors who routinely ask about other safety issues, such as using car seats and wearing helmets while riding bikes.
“We can all agree that children should never be injured by a gun."
“We can all agree that children should never be injured by a gun."
A federal judge struck down Florida’s 2011 law that forbade doctors to ask about guns in the home, but the NRA has promoted similar legislation in a dozen other states, according to Everytown, a group that advocates against firearms violence.
The NRA also opposes preventing teens from buying semi-automatic weapons. “Legislative proposals to prevent law-abiding adults aged 18-20 years old from acquiring semi-automatic rifles would deny them access to the most modern and effective rifles for self-defense, thus depriving them of their constitutional rights,” it says.
Hoffman said lawmakers should sponsor research into the best ways to prevent gun violence and gun accidents and then act on what the research shows — whether that means limits on gun ownership, or something else. “We are in a country where kids and guns are going to coexist,” Hoffman said.
The Centers for Disease Control and Prevention has been restricted from performing or paying for gun violence research by federal legislation called the Dickey Amendment, which has language that CDC scientists interpret as meaning they had better stay away from the subject.
Hoffman says that’s a mistake. “We need to acknowledge that it is a public health problem,” he said.
“The amazing scientists at the CDC are looking for the best available evidence,” he added. “Their mission is to protect Americans from threats to their health.”
Hoffman noted that an average of 74 children and teenagers under the age of 21 are killed or severely injured by guns.
“If there were 74 kids critically ill and dying from flu every single day, we would spring to action,” he said. The CDC has reports of 142 children who have died from influenza since October, or about 20 a month on average.
Related
Pediatricians take on gun lobby -- very carefully
The three-year-old whose death still haunts Hoffman was killed by a handgun kept in a parent’s bedside table. Many advocates say keeping kids away from guns is a matter of discipline and responsibility, but Hoffman said that’s a fallacy.
“You need to think about how kids are different from adults. Kids are inherently curious and impulsive,” he said.
Hoffman said he does not necessarily support asking people to give up guns. “With rights come responsibilities,” he said. “When I think back to the toddler who died — if that gun had been stored in a locked gun safe, that child would have been safe.”
'''
stopwords = [' ','the','to','that','and','said','for','are','about','has','who','a','from','on','in','by','of','we','is','The','We','be','can','he','been','never','at','or','should','\n']
puncs = '！？｡＂＃＄％＆＇（）＊＋，－／：；＜＝＞＠［＼］＾＿｀｛｜｝～｟｠｢｣､、〃》「」『』【】〔〕〖〗〘〙〚〛〜〝〞〟〰〾〿–—‘’‛“”„‟…‧﹏.。,'
seg_list = jieba.cut(demo_text, cut_all=False)  # 精确模式
print("Default Mode: " + "/ ".join(seg_list))

seg_list = jieba.cut(demo_text, cut_all=False)
seg_list = list(seg_list)
wordDict = {}
for w in seg_list:
    if (w not in stopwords) and (w not in puncs):
        if w in wordDict:
            wordDict[w] = wordDict[w] + 1
        else:
            wordDict[w] = 1
print(wordDict)
font = r"d:\\wqy-microhei.ttc"
wordcloud = WordCloud(font_path=font)
wordcloud.fit_words(wordDict)
plt.imshow(wordcloud)