
```
START
  INPUT NAME;
    WHILE name IS empty:
    input name;

OUTPUT welcome message with name;

  WHILE counter <10:
  GENERATE number1;
  GENERATE number2;
  GENERATE operator;

  PRINT question;
  INPUT answer;
  IF answer IS correct:
    OUTPUT correct message;
    score + 1;
  ELSE:
    OUTPUT inncorrect message;

  counter + 1;
  
PRINT score with well done message;
END;
```
