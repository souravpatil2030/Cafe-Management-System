import 'package:flutter/material.dart';

class RulesPage extends StatefulWidget {
  @override
  _RulesPageState createState() => _RulesPageState();
}

class _RulesPageState extends State<RulesPage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Scratch and Win"),
      ),
      body: Center(
        child: Text("The rules for this game are pretty simple"),
	      child: Text("• Only one order at a time"),
	      child: Text("• No demands for special services"),
	      child: Text("• use only for fun"),
      ),
    );
  }
}
