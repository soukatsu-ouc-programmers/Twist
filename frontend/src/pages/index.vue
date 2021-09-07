<template>
  <div>
    <h1 class="page-title">
      ページ名
    </h1>
    <table>
      <thead>
        <tr>
          <td />
          <td>
            <ColumnTitle />
          </td>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>
            <Time :since="'10:00'" :until="'11:00'" />
          </td>
          <td class="session-cell">
            <Session />
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<style lang="scss" scoped>
  .page-title{
    margin-top: 2rem;
    margin-bottom: 2rem;
    margin-left: 2rem;
  }
  table{
    margin: 0 0 275px 0;
  }
  td{
    padding: 10px 20px;
    white-space: pre-wrap;
  }
</style>

<script>
export default {}
</script>
