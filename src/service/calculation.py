class CalculationService:
    def get_output(self) -> str:

        #演算処理関連の動作確認実施
        output = '【演算処理】<br>'
        output = output + '<br>'
        output = output + '足し算<br>'
        output = output + '7 + 2 = ' + str( 7 + 2 ) + '<br>'
        output = output + '<br>'
        output = output + '引き算<br>'
        output = output + '7 - 2 = ' + str( 7 - 2 ) + '<br>'
        output = output + '<br>'
        output = output + '掛け算<br>'
        output = output + '7 * 2 = ' + str( 7 * 2 ) + '<br>'
        output = output + '<br>'
        output = output + 'べき乗<br>'
        output = output + '7 ** 2 = ' + str( 7 ** 2 ) + '<br>'
        output = output + '<br>'
        output = output + '割り算<br>'
        output = output + '7 / 2 = ' + str( 7 / 2 ) + '<br>'
        output = output + '<br>'
        output = output + '整数除算<br>'
        output = output + '7 // 2 = ' + str( 7 // 2 ) + '<br>'
        output = output + '<br>'
        output = output + '余剰<br>'
        output = output + '7 % 2 = ' + str( 7 % 2 ) + '<br>'
        output = output + '<br>'

        output = output + '実数での除算<br>'
        output = output + '7 / 1 = ' + str( 7 / 1 ) + '<br>'
        output = output + '7 / 2 = ' + str( 7 / 2 ) + '<br>'
        output = output + '1 / 3 = ' + str( 1 / 3 ) + '<br>'
        output = output + '1 / 1 = ' + str( 1 / 1 ) + '<br>'
        output = output + '<br>'
        output = output + '整数での除算<br>'
        output = output + '7 // 1 = ' + str( 7 // 1 ) + '<br>'
        output = output + '7 // 2 = ' + str( 7 // 2 ) + '<br>'
        output = output + '1 // 3 = ' + str( 1 // 3 ) + '<br>'
        output = output + '<br>'
        output = output + '余剰<br>'
        output = output + '7 % 1 = ' + str( 7 % 1 ) + '<br>'
        output = output + '7 % 2 = ' + str( 7 % 2 ) + '<br>'
        output = output + '1 % 3 = ' + str( 1 % 3 ) + '<br>'
        output = output + '1 % 1 = ' + str( 1 % 1 ) + '<br>'
        output = output + '999 % 1000 = ' + str( 999 % 1000 ) + '<br>'
        output = output + '<br>'

        output = output + 'ゼロ除算<br>'
        try:
            output = output + '1 / 0 = ' + str( 1 / 0 ) + '<br>'
        except ZeroDivisionError as e:
            output = output + '1 / 0 = ' + str(e) + '<br>'
        try:
            output = output + '1 // 0 = ' + str( 1 // 0 ) + '<br>'
        except ZeroDivisionError as e:
            output = output + '1 // 0 = ' + str(e) + '<br>'
        try:
            output = output + '1 % 0 = ' + str( 1 % 0 ) + '<br>'
        except ZeroDivisionError as e:
            output = output + '1 % 0 = ' + str(e) + '<br>'

        output = output + '<br>'
        
        import math
        output = output + '平方根<br>'
        output = output + 'math.sqrt(2) = ' + str( math.sqrt(2) ) + '<br>'
        output = output + '<br>'
        output = output + '円周率<br>'
        output = output + 'math.pi = ' + str( math.pi ) + '<br>'
        output = output + '<br>'
        output = output + '<br>'
        output = output + '【練習問題】<br>'
        output = output + '1.次の三角形の面積を求めなさい<br>底辺：4cm、高さ6cm<br>12㎠になるはずです。<br>'
        output = output + '4 * 6 / 2 = ' + str(  4 * 6 / 2 ) + '<br>'
        output = output + '<br>'
        output = output + '2.次の立方体の体積を求めなさい<br>一辺の長さ：3cm<br>27㎤になるはずです。<br>※計算は２項演算子で行うこと。<br>'
        output = output + '3 ** 3 = ' + str(3 ** 3) + '<br>'
        output = output + '<br>'
        output = output + '3.黄金比を求めてください。<br>黄金比とは、5 の平方根に 1 を加えて 2 で割ったものです。<br>約 1.618 になるはずです。<br>'
        output = output + '( math.sqrt(5) + 1 ) / 2 = ' + str( ( math.sqrt(5) + 1 ) / 2 ) + '<br>'
        output = output + '<br>'
            

        return output