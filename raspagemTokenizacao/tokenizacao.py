
import nltk
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.tokenize.treebank import TreebankWordTokenizer
import re




def print_tokens(tk):
    tc = 1
    print('Total tokens: ', len(tk))
    for token in tk:
        print("Token #", tc, ":", token)
        tc += 1

text = '''Having the sort of ears that in-ear buds don't seem to agree with I generally go for the open ear design...The battery life appears to be around the average for ear buds, especially when you turn ANC off (which doesn't seem to do anything noticeable anyway), the quality is very good although this should be expected due to the price of them.Connectivity (especially to a Samsung phone) was easy and the phone picked them up as soon as I opened the case, the inclusion of wireless charging should be a given at the price, although I have paid more for Bose ear buds that do not include it.The last thing I will address is value for money and also sound quality, I got these at the offer price of £129, I don't think I would pay full price for them as Samsung regularly run discounts and offers on most of their products, although I have a pair of Bose quiet comfort 2 ear buds and also a pair of Google pixel buds pro, I prefer the fit of these Samsung buds, the sound quality of the Bose and Google buds (along with the ANC is obviously better due to the in ear design) however, these open ear buds are still very good sonically, my previous go-to open ear buds were Soundpeats 3, the Samsung buds sound much better than those and have better bass and clarity.I have seen a lot of people mention the fit and comfort of these Samsung buds, I have personally had absolutely no issues with either, they feel comfortable in my ears and have had no issues with them falling out etc, however, I'm well 
aware that everyone has different shaped ears so my advice would be to buy them, try them and return them if they do not fit.
Read more
One person found this helpful'''

def tolkenizar(text):
    default_sentence_tokenizer = nltk.sent_tokenize
    fixed_text = re.sub(r"(?<!\s)(\.)([A-Z])", r"\1 \2", text)
    basic_sentence_tokens_en = default_sentence_tokenizer(text=fixed_text)
    print("Total nltk sentece tokenizer tokens: ", len(basic_sentence_tokens_en))
    print_tokens(basic_sentence_tokens_en)
    return basic_sentence_tokens_en


#tolkenizar(text)
# sent_tokenize nltk sentence tokenize
# default_sentence_tokenizer = nltk.sent_tokenize


# basic_sentence_tokens_en = default_sentence_tokenizer(text=sample_text_en)
# print("English:")
# print("Total nltk sentece tokenizer tokens: ", len(basic_sentence_tokens_en))
# print_tokens(basic_sentence_tokens_en)
# print("\n\n")

