import java.util.*;
import java.io.*;

class Solution{
    static class FastReader{
        BufferedReader br;
        StringTokenizer st;
        public FastReader(){
            br=new BufferedReader(new InputStreamReader(System.in));
        }
        String next(){
            while(st==null || !st.hasMoreTokens()){
                try {
                    st=new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }
        int nextInt(){
            return Integer.parseInt(next());
        }
        long nextLong(){
            return Long.parseLong(next());
        }
        double nextDouble(){
            return Double.parseDouble(next());
        }
        String nextLine(){
            String str="";
            try {
                str=br.readLine().trim();
            } catch (Exception e) {
                e.printStackTrace();
            }
            return str;
        }
    }
    static class FastWriter {
		private final BufferedWriter bw;

		public FastWriter() {
			this.bw = new BufferedWriter(new OutputStreamWriter(System.out));
		}

		public void print(Object object) throws IOException {
			bw.append("" + object);
		}

		public void println(Object object) throws IOException {
			print(object);
			bw.append("\n");
		}

		public void close() throws IOException {
			bw.close();
		}
	}
    static int[] string_to_array(String[] arr){
        int[] ans=new int[arr.length];
        for(int i=0;i<arr.length;i++){
            ans[i]=Integer.parseInt(arr[i]);
        }
        return ans;
    }
    public static void main(String[] args) {
        try {
            FastReader in=new FastReader();
            FastWriter out = new FastWriter();
            int testCases=in.nextInt();
            while(testCases-- > 0){
                int n=Integer.parseInt(in.nextLine());
				String s=in.nextLine();
				int one=0;
				int zero=0;
				for(int i=0;i<s.length();i++){
					if(s.charAt(i)=='0'){
						zero++;
					}else{
							one++;
					}
				}
				//out.println(zero+" "+one);
				if(zero==n || one==n){
					out.println("YES");
					continue;
				}
				if(n%2==0){
					if(one%2==0 && zero%2==0){
						out.println("YES");
					}
					else if(zero==one){
						out.println("YES");
					}else{
						out.println("NO");
					}
				}else{
					if (one > zero)
					{
						if ((one - zero) % 2 == 1)
						{
							out.println("YES");
						}
						else
						{
							out.println("No");
						}
					}
				else
				{
					if ((zero - one) % 2 == 1)
					{
						out.println("YES");
					}
					else{
						out.println("YES");
					}
				}
			}

            }
            out.close();
        } catch (Exception e) {
            return;
        }
    }
}



