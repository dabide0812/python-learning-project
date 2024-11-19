class StringService:
    def get_output(self) -> str:

        #演算処理関連の動作確認実施
        output = ''
        output = output + '足し算<br>'
        output = output + '7 + 2 = ' + str( 7 + 2 ) + '<br><br>'
        output = output + '引き算<br>'
        output = output + '7 - 2 = ' + str( 7 - 2 ) + '<br><br>'
        output = output + '掛け算<br>'
        output = output + '7 * 2 = ' + str( 7 * 2 ) + '<br><br>'
        output = output + 'べき乗<br>'
        output = output + '7 ** 2 = ' + str( 7 ** 2 ) + '<br><br>'
        output = output + '割り算<br>'
        output = output + '7 / 2 = ' + str( 7 / 2 ) + '<br><br>'
        output = output + '整数除算<br>'
        output = output + '7 // 2 = ' + str( 7 // 2 ) + '<br><br>'
        output = output + '余剰<br>'
        output = output + '7 % 2 = ' + str( 7 % 2 ) + '<br><br>'

        return output