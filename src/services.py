class StringService:
    def get_output(self) -> str:

        #演算処理関連の動作確認実施
        output = ''
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
            

        return output