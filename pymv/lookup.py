class Lookup:
    @staticmethod
    def get_master_display(color_primaries):
        # see here for values: https://github.com/SK-Hardwired/nv_hevc_hdr_patcher/issues/9#issuecomment-392572348
        
        if color_primaries == "bt2020":
            return "G(8500|39850)B(6550|2300)R(35400|14600)WP(15635|16450)L(10000000|1)"
        elif color_primaries == "bt709" or color_primaries == "unknown":
            return "G(15000|30000)B(7500|3000)R(32000|16500)WP(15635|16450)L(10000000|1)"
        elif color_primaries == "display-p3":
            return "G(13250|34500)B(7500|3000)R(34000|16000)WP(15635|16450)L(10000000|1)"
        raise ValueError("Unknown color primary")