from PyQt4.QtGui import *
from PyQt4.QtCore import *
class Highlighter(QSyntaxHighlighter):
    def __init__(self, parent=None):
        super(Highlighter, self).__init__(parent)


        quotationColor = "rgb(195,232,141)"
        classfunctionColor = "rgb(255,203,107)"
        keywordColor = "rgb(183,146,234)"
        functionColor = "rgb(137,215,217)"
        commentColor = "rgb(247,118,105)"


        keywordFormat = QTextCharFormat()
        keywordFormat.setForeground(QColor(183,146,234))
        keywordFormat.setFontWeight(QFont.Bold)
        keywordPatterns = ["\\bFalse\\b", "\\bNone\\b", "\\bTrue\\b", "\\band\\b", "\\bas\\b",
                           "\\bassert\\b", "\\bbreak\\b", "\\bcontinue\\b",
                           "\\bdel\\b", "\\belif\\b", "\\belse\\b", "\\bexcept\\b", "\\bfinally\\b",
                           "\\bfor\\b", "\\bfrom\\b", "\\bglobal\\b", "\\bif\\b", "\\bimport\\b",
                           "\\bin\\b", "\\bis\\b", "\\blambda\\b", "\\bnonlocal\\b", "\\bnot\\b",
                           "\\bor\\b", "\\bpass\\b", "\\braise\\b", "\\breturn\\b", "\\btry\\b",
                           "\\bwhile\\b", "\\bwith\\b", "\\byield\\b", "\\print\\b"] 
        self.highlightingRules = [(QRegExp(pattern), keywordFormat)
                for pattern in keywordPatterns]


        classRegExp = "\\bclass\s[A-Za-z_]+\\b"
        classFormat = QTextCharFormat()
        classFormat.setForeground(QColor(255,203,107))
        classFormat.setFontWeight(QFont.Bold)
        self.highlightingRules.append((QRegExp(classRegExp), classFormat))


        defRegExp = "\\bdef\s[A-Za-z_0-9_]+\\b"
        defFormat = QTextCharFormat()
        defFormat.setForeground(QColor(255,203,107))
        defFormat.setFontWeight(QFont.Bold)
        self.highlightingRules.append((QRegExp(defRegExp), defFormat))


        singleLineCommentExp = "#[^\n]*"
        singleLineCommentFormat = QTextCharFormat()
        singleLineCommentFormat.setForeground(QColor(247,118,105))
        self.highlightingRules.append((QRegExp(singleLineCommentExp), singleLineCommentFormat))


        quotationExp = "\".*\""
        
        quotationFormat = QTextCharFormat()
        quotationFormat.setForeground(QColor(195,232,141))
        self.highlightingRules.append((QRegExp(quotationExp), quotationFormat))
    

        functionExp = "\\[A-Za-z0-9_]+(?=\\()"
        functionFormat = QTextCharFormat()
        functionFormat.setForeground(QColor(137,215,217))
        functionFormat.setFontWeight(QFont.Bold)
        self.highlightingRules.append((QRegExp(functionExp), functionFormat))
        

    def highlightBlock(self, text):
        for pattern, format in self.highlightingRules:
            expression = QRegExp(pattern)
            index = expression.indexIn(text)
            while index >= 0:
                length = expression.matchedLength()
                self.setFormat(index, length, format)
                index = expression.indexIn(text, index + length)

        self.setCurrentBlockState(0)
