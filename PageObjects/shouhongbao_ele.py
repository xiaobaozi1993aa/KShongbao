from Common.Basepage import Basepage

class Shouhongbao(Basepage):

    user_id = 'id**com.sz.gcyh.KSHongBao:id/take_red_packet_user_iv'    #个人
    message_id = 'id**com.sz.gcyh.KSHongBao:id/take_red_packet_message_iv'  #消息
    castellan_id = 'id**com.sz.gcyh.KSHongBao:id/take_red_packet_duke_iv'   #城主
    agency_id = 'id**com.sz.gcyh.KSHongBao:id/take_red_packet_agent_tv' #代理
    share_id = 'id**com.sz.gcyh.KSHongBao:id/take_red_packet_share_dig_rl'  #分享
    take_red_id = 'id**com.sz.gcyh.KSHongBao:id/take_red_packet_out_packet_iv'   #发红包
    information_id = 'id**com.sz.gcyh.KSHongBao:id/home_information_iv' #资讯
    play_game_id = 'id**com.sz.gcyh.KSHongBao:id/home_play_game_iv' #蜜玩
    home_take_red_id = 'id**com.sz.gcyh.KSHongBao:id/home_take_red_packet_iv'   #收红包
    bussniss_id = 'id**com.sz.gcyh.KSHongBao:id/home_business_circle_iv'    #商圈
    money_id = 'id**com.sz.gcyh.KSHongBao:id/home_wallet_iv'    #钱包
    fresh_id = 'id**com.sz.gcyh.KSHongBao:id/take_red_packet_refresh_iv'    #刷新
    back_id = 'id**com.sz.gcyh.KSHongBao:id/person_back_iv' #返回

    def shouhongbao(self):
        self.find_element(self.user_id).click()
        self.find_element(self.back_id).click()

    def liucheng(self):
        self.find_element(self.play_game_id).click()
        self.find_element(self.information_id).click()
