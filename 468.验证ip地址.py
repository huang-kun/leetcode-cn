#
# @lc app=leetcode.cn id=468 lang=python3
#
# [468] 验证IP地址
#

# @lc code=start
class Solution:
    def validIPAddress(self, IP: str) -> str:
        # 验证IPv4
        if '.' in IP:
            # 地址包含4个十进制数
            components = IP.split('.')
            if len(components) != 4:
                return "Neither"

            for component in components:
                num_len = len(component)
                # 每个区域段必须是数字
                if not component.isnumeric():
                    return "Neither"
                # 数字区间为0-255
                if num_len == 0 or num_len > 3:
                    return "Neither"
                num = int(component)
                if num < 0 or num > 255:
                    return "Neither"
                # 数字不可以0开头，比如01
                if num_len > 1 and component[0] == '0':
                    return "Neither"
            
            return "IPv4"

        # 验证IPv6
        elif ':' in IP:
            # 地址由8组16进制的数字来表示
            components = IP.split(':')
            if len(components) != 8:
                return "Neither"
            
            hex_digits = "0123456789abcdef"
            for component in components:
                num_len = len(component)
                # 每组表示16比特，所以换算成16进制数的话，最多4个数字
                if num_len > 4 or num_len == 0:
                    return "Neither"
                # 数字必须是16进制
                for digit in component:
                    if not digit.lower() in hex_digits:
                        return "Neither"

            return "IPv6"

        return "Neither"
        
# @lc code=end

if __name__ == "__main__":
    s = Solution()
    s.validIPAddress("172.16.254.1") == "IPv4"
    s.validIPAddress("256.256.256.256") == "Neither"
    s.validIPAddress("2001:0db8:85a3:0000:0000:8a2e:0370:7334") == "IPv6"
    s.validIPAddress("2001:db8:85a3:0:0:8A2E:0370:7334") == "IPv6"
    s.validIPAddress("2001:0db8:85a3::8A2E:0370:7334") == "Neither"
    s.validIPAddress("02001:0db8:85a3:0000:0000:8a2e:0370:7334") == "Neither"

