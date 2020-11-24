# int main()
# {
# 	int N, M, id, opr, score[10], max_score[10], score_buffer, id_buffer, max_buffer;
# 	int globe_k, k;
# 	char opr_char;
# 	while (cin >> N >> M) 	{
# 		globe_k = 0;
# 		for (id = 0; id < N; id++)
# 			cin >> score[id];
# 		for (opr = 0; opr < M; opr++) {
# 			cin >> opr_char >> id_buffer >> score_buffer;
# 			if (opr_char == 'Q') { // 读操作
# 				max_buffer = 0;
# 				if(score_buffer > id_buffer) // 判断范围
# 					for (id = id_buffer - 1; id < score_buffer; id++)
# 						max_buffer = (max_buffer < score[id]) ? score[id] : max_buffer;
# 				else 
# 					for (id = score_buffer - 1; id < id_buffer; id++)
# 						max_buffer = (max_buffer < score[id]) ? score[id] : max_buffer;
# 				max_score[globe_k++] = max_buffer;   // 装载进行数组（其实也可以直接输出）
# 			}
# 			else                      // 写操作
# 				score[id_buffer - 1] = score_buffer;
# 		}
# 		for (k = 0; k < globe_k; k++)  // 输出
# 			cout << max_score[k] << endl;
# 	}
# 	return 0;
# }
while True:
    try:
        N, M = [int(each) for each in input().split()]
        scores = [int(each) for each in input().split()]
        operations = []
 
        for i in range(M):
            operations.append(input().split())
        results = []
        for each in operations:
            if each[0] == 'U':
                scores[int(each[1]) - 1] = int(each[2])
                continue
            else:
                front = min(int(each[1]), int(each[2]))
                back = max(int(each[1]), int(each[2]))
                max_ = 0
                for j in range(front-1, back):
                    if scores[j] > max_:
                        max_ = scores[j]
                results.append(max_)
 
        for each in results:
            print(each)
    except:
        break