# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        
        def hostname(starturl):
            return starturl.split('/')[2]

        start_url = hostname(startUrl)
        visited = set()

        def dfs(url, parser):

            visited.add(url)
            for next_url in parser.getUrls(url):
                if hostname(next_url) == start_url and next_url not in visited:
                    dfs(next_url, parser)


        dfs(startUrl,htmlParser )


        return visited