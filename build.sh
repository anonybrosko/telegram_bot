if git add .; then
  if git commit -m "${1}"; then
    git push
  fi
fi
