class Solution:
	def addBinary(self, s1, s2):
		res = ""
		carr = 0
		a,b = s1[::-1],s2[::-1]
		for i in range(max(len(a),len(b))):
			bit1 = ord(a[i]) - ord("0") if i < len(a) else 0
			bit2 = ord(b[i]) - ord("0") if i < len(b) else 0
			tot = bit1+bit2+carr
			res = str(tot%2)+res
			carr= tot //2
		if carr:
		   res = '1'+res
		return res.lstrip('0') 