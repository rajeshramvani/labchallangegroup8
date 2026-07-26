2001  mkdir lab8
 2002  cd lab8
 2003  git init
 2004  git add README.md
 2005  vi README.md
 2006  git add README.md 
 2007  git commit -m "readme group8"
 2008  git branch -M main
 2009  git remote add origin https://github.com/rajeshramvani/labchallangegroup8.git
 2010  git push origin main
 2011  vi .git/config 
 2012  git push origin main
 2013  git -b rajesh
 2014  git -c rajesh
 2015  clear
 2016  git checkout -b rajeshg8
 2017  git status
 2018  git switch -c rajeshg8
 2019  git status
 2020  git add payment.html 
 2021  ll
 2022  git commit -m "payment page added in rajeshg8 branch"
 2023  vi .git/config 
 2024  git push origin rajeshg8
 2025  git status
 2026  git add index.html
 2027  git commit -m "commit the index file"
 2028  git push origin rajeshg8 
 2029  git checkout main
 2030  git status
 2031  ll
 2032  git merge rajeshg8 
 2033  git status
 2034  ll
 2035  git push origin main
 2036  git status
 2037  git checkout main
 2038  git status
 2039  git history
 2040  history
 2041  git checkout main
 2042  git status
 2043  git pull origin main