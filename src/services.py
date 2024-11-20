class StringService:
    def get_output(self) -> str:

        #演算処理関連の動作確認実施
        
        import math

        output = ''
        output = output + '平方根<br>'
        output = output + 'math.sqrt(2) = ' + str( math.sqrt(2) ) + '<br>'
        output = output + '<br>'
        output = output + '円周率<br>'
        output = output + 'math.pi = ' + str( math.pi ) + '<br>'
        output = output + '<br>'
        output = output + '円周率<br>'
        output = output + 'math.pi = ' + str( math.pi ) + '<br>'
        output = output + '<br>'
        output = output + '練習問題<br>'
        output = output + '黄金比を求めてください。黄金比とは、5 の平方根に 1 を加えて 2 で割ったものです。約 1.618 になるはずです。<br>'
        output = output + '( math.sqrt(5) + 1 ) / 2 = ' + str( ( math.sqrt(5) + 1 ) / 2 ) + '<br>'
            

        return output