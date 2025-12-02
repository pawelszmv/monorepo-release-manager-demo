import React from 'react';
import { SafeAreaView, Text, View, Button, StyleSheet } from 'react-native';
import packageInfo from './package.json';

export default function App() {
  return (
    <SafeAreaView style={styles.container}>
      <View>
        <Text style={styles.title}>Mobile App (React Native)</Text>
        <Text>Version: {packageInfo.version}</Text>
        <View style={{ height: 12 }} />
        <Button title="Ping" onPress={() => alert('pong')} />
      </View>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, justifyContent: 'center', padding: 20 },
  title: { fontSize: 20, marginBottom: 8 }
});